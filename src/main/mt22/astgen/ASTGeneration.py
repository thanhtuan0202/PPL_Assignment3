#my student id: 2014931
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decllist = []
        for x in ctx.declaration():
            decl = self.visitDeclaration(x)
            if isinstance(decl,list):
                decllist.extend(decl if decl else [])
            else:
                decllist.append(decl)
        return Program(decllist)
    def visitDeclaration(self,ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)
    def visitVardecl(self,ctx: MT22Parser.VardeclContext):
        if ctx.varwithexprdecl():
            data = self.visit(ctx.varwithexprdecl()) #[(a,b,c),(int,'',''),(1,2,3)]
            idlist = data[0][::-1]
            typ = data[1]
            expr = data[2]
            return [VarDecl(idlist[i],typ[0],expr[i]) for i in range(len(idlist))]
        name = []
        name = self.visit(ctx.varlist())
        typ = self.visit(ctx.mt_type()) if ctx.mt_type() else AutoType()
        return [VarDecl(i,typ) for i in name]
    def visitVarlist(self,ctx:MT22Parser.VarlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        return self.visit(ctx.varlist()) + [ctx.IDENTIFIER().getText()]

    def visitVarwithexprdecl(self,ctx:MT22Parser.VarwithexprdeclContext):
        if ctx.varini():
            return self.visit(ctx.varini()) #(c,int,1)
        #a,b,c : int = 1,2,3
        name = ctx.IDENTIFIER().getText() 
        ele = self.visit(ctx.varwithexprdecl()) 
        expr = self.visit(ctx.expr())
        ele[0] = ele[0]+ [name]
        ele[2] = ele[2]+ [expr]
        return ele      
    def visitVarini(self,ctx: MT22Parser.VariniContext):
        name = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.mt_type()) if ctx.mt_type() else AutoType()
        ini = self.visit(ctx.expr())
        return [[name],[typ], [ini]]
   
    #function declaration
    def visitFuncdecl(self,ctx: MT22Parser.FuncdeclContext):
        name = ctx.IDENTIFIER().getText()
        type = self.visit(ctx.return_type())
        params = self.visit(ctx.paralist()) if ctx.paralist() else []
        inherit = self.visit(ctx.inherit()) if ctx.inherit() else None
        blockstmt = self.visit(ctx.block_stmt())
        return FuncDecl(name,type,params,inherit,blockstmt)
    
    def visitInherit(self,ctx: MT22Parser.InheritContext):
        return ctx.IDENTIFIER().getText()
    def visitReturn_type(self,ctx: MT22Parser.Return_typeContext):
        if ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        return self.visit(ctx.mt_type())

    def visitParalist(self,ctx: MT22Parser.ParalistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameter())]
        return self.visit(ctx.paralist()) +  [self.visit(ctx.parameter())]
    
    #parameter declaration
    def visitParameter(self,ctx: MT22Parser.ParameterContext):
        name = ctx.IDENTIFIER().getText()
        type = self.visit(ctx.mt_type()) if ctx.mt_type() else AutoType()
        out = True if ctx.OUT() else False
        inherit = True if ctx.INHERIT() else False
        return ParamDecl(name,type,out,inherit)
    def visitMt_type(self,ctx: MT22Parser.Mt_typeContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        return self.visit(ctx.array_type())
   
    #stmt declarations
    def visitStmt(self,ctx: MT22Parser.StmtContext):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        elif ctx.do_while_stmt():
            return self.visit(ctx.do_while_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        else: return self.visit(ctx.call_stmt())
   
    #assign stmt
    def visitAssign_stmt(self, ctx: MT22Parser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.expr())
        return AssignStmt(lhs, expr)
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return self.visit(ctx.index_op())
   
    #if statement
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        if ctx.fullif():
            return self.visit(ctx.fullif())
        return self.visit(ctx.halfif())
    def visitFullif(self,ctx:MT22Parser.FullifContext):
        expr = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt(0))
        fstmt = self.visit(ctx.stmt(1))
        return IfStmt(expr,tstmt,fstmt)
    def visitHalfif(self,ctx: MT22Parser.HalfifContext):
        if ctx.halfif():
            expr = self.visit(ctx.expr())
            tstmt = self.visit(ctx.fullif()) if ctx.fullif() else self.visit(ctx.stmt())
            fstmt = self.visit(ctx.halfif())
            return IfStmt(expr,tstmt,fstmt)
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return IfStmt(expr,stmt,None)
    
    #for statements
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        init = self.visit(ctx.init_expr())
        condexpr = self.visit(ctx.cond_expr())
        updateexpr = self.visit(ctx.update_expr())
        stmt = self.visit(ctx.stmt())
        return ForStmt(init,condexpr,updateexpr,stmt)
    def visitInit_expr(self,ctx: MT22Parser.Init_exprContext):
        lhs = Id(ctx.IDENTIFIER().getText())
        expr = self.visit(ctx.expr())
        return AssignStmt(lhs, expr)
    def visitCond_expr(self, ctx: MT22Parser.Cond_exprContext):
        return self.visit(ctx.expr())
    def visitUpdate_expr(self, ctx: MT22Parser.Update_exprContext):      
        return self.visit(ctx.expr())
    
    #while + do while statement
    def visitWhile_stmt(self,ctx: MT22Parser.While_stmtContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(expr, stmt)
    def visitDo_while_stmt(self, ctx: MT22Parser.Do_while_stmtContext):
        expr = self.visit(ctx.expr())
        blockstmt = self.visit(ctx.block_stmt())
        return DoWhileStmt(expr, blockstmt)
    #return statement
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        expr = self.visit(ctx.expr())
        return ReturnStmt(expr)
    #call statements
    
    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        id = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.exprlist()) if ctx.exprlist() else []
        return CallStmt(id,expr)
    
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return self.visit(ctx.exprlist()) + [self.visit(ctx.expr())]
    
    # break statement
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()
    
    #continue statement
    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return ContinueStmt()
    
    #block statements
    def visitBlock_stmt(self,ctx: MT22Parser.Block_stmtContext):
        body = self.visit(ctx.body())
        return BlockStmt(body)
        #return BlockStmt([])
    
    def visitBody(self, ctx: MT22Parser.BodyContext):
        if ctx.bodypara():
            return self.visit(ctx.bodypara()) + self.visit(ctx.body())
        return []
    
    def visitBodypara(self,ctx:MT22Parser.BodyparaContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())]
        return self.visit(ctx.vardecl())
    #expression
    def visitExpr(self,ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1())
        left = self.visit(ctx.expr())
        right = self.visit(ctx.expr1())
        op = ctx.SCOPE().getText()
        return BinExpr(op, left, right)
    def visitExpr1(self,ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        op = self.visit(ctx.relational())
        return BinExpr(op, left, right)
    def visitExpr2(self,ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
        return BinExpr(op, left, right)
    def visitExpr3(self,ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
        return BinExpr(op, left, right)
    def visitExpr4(self,ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        op = self.visit(ctx.mul_div())
        return BinExpr(op, left, right)
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        op = ctx.NOT().getText()
        expr = self.visit(ctx.expr6())
        return UnExpr(op,expr)
    def visitExpr6(self,ctx:MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        sign = ctx.SUB().getText();
        expr = self.visit(ctx.expr7())
        return UnExpr(sign, expr)
    def visitExpr7(self,ctx:MT22Parser.Expr7Context):
        return self.visit(ctx.operands())
    
    #operands
    def visitOperands(self,ctx:MT22Parser.OperandsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.literial():
            return self.visit(ctx.literial())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.index_op():
            return self.visit(ctx.index_op())
        return self.visit(ctx.expr())
    
    def visitLiterial(self,ctx:MT22Parser.LiterialContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLit(ctx.BOOLLIT().getText())
        return self.visit(ctx.arraylit())
    
    def visitFunc_call(self,ctx:MT22Parser.Func_callContext):
        id = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.exprlist()) if ctx.exprlist() else []
        return FuncCall(id,expr)
    
    def visitIndex_op(self,ctx:MT22Parser.Index_opContext):
        id = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.exprlist())
        return ArrayCell(id,expr)
    
    def visitMul_div(self,ctx:MT22Parser.Mul_divContext):
        if ctx.MUL():
            return ctx.MUL().getText()
        elif ctx.DIV():
            return ctx.DIV().getText()
        return ctx.MOD().getText()
    
    def visitRelational(self,ctx:MT22Parser.RelationalContext):
        if ctx.EQUALTO():
            return ctx.EQUALTO().getText()
        elif ctx.NOTEQ():
            return ctx.NOTEQ().getText()
        elif ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.GREAT():
            return ctx.GREAT().getText()
        elif ctx.GREATEQ():
            return ctx.GREATEQ().getText()
        return ctx.LESSEQ().getText()
    #atomic type
    def visitAtomic_type(self,ctx:MT22Parser.Atomic_typeContext):
        if ctx.INTEGER(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.STRING(): return StringType()
        if ctx.BOOLEAN(): return BooleanType()
        
    def visitArray_type(self,ctx:MT22Parser.Array_typeContext):
        dimensions = self.visit(ctx.intlist())
        atotype = self.visit(ctx.atomic_type()) if ctx.atomic_type() else AutoType()
        return ArrayType(dimensions,atotype)
    def visitIntlist(self,ctx:MT22Parser.IntlistContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return self.visit(ctx.intlist()) + [int(ctx.INTLIT().getText())]
    
    def visitArraylit(self,ctx:MT22Parser.ArraylitContext):
        if ctx.arraylit_para():
            return self.visit(ctx.arraylit_para())
        return self.visit(ctx.arraylitlist())
    
    def visitArraylitlist(self,ctx:MT22Parser.ArraylitlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arraylit_para())
        return self.visitArraylitlist(ctx.arraylitlist()) + self.visit(ctx.arraylit_para())
    
    def visitArraylit_para(self, ctx:MT22Parser.Arraylit_paraContext):
        expr = self.visit(ctx.exprlist()) if ctx.exprlist() else []
        return ArrayLit(expr)
    
    