# My student ID: 2014931
#
import sys
from functools import reduce

sys.path.append('../../../../target/main/mp/parser')
sys.path.append('../utils')
from StaticError import *
from Utils import Utils
from Visitor import *
from AST import *
from abc import ABC
    
class MType:
    # type of function
    def __init__(self, partype, rettype, inherit=None):
        self.partype = partype  # list type of param
        self.rettype = rettype  # return type
        self.inherit = inherit  # parent function

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + str(self.inherit) + ')'


class Symbol:

    def __init__(self,kind, name, mtype, value=None, inherit: bool = False, out: bool = False):
        self.kind = kind
        self.name = name
        self.mtype = mtype
        self.value = value
        self.inherit = inherit
        self.out = out

    def __str__(self):
        return "{}{}Symbol({}, {},{})".format("Inherit" if self.inherit else "", "Out" if self.out else "", self.name,
                                              str(self.mtype), str(self.value))

    def toTupleString(self):
        return (str(self.name).lower(), str(self.mtype))

class ExpUtils:
    @ staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntegerType, FloatType]

class GetEnv(Visitor, Utils):
    def __init__(self):
        self.globalEnv = []
    def visitProgram(self, ast: Program, o: object):
        o = self.globalEnv
        for decl in ast.decls:
            if type(decl) is VarDecl:
                o += [self.visit(decl, o)]
            else:
                o = self.visit(decl, o)
        return o

    def visitVarDecl(self, ast: VarDecl, o: object):
        return Symbol(Variable(),ast.name, ast.typ, ast.init)

    def visitParamDecl(self, ast: ParamDecl, o: object):
        return Symbol(Parameter(),ast.name, ast.typ, None, ast.inherit, ast.out)

    def visitFuncDecl(self, ast: FuncDecl, o: object):
        paratype = []
        paratype += [self.visit(x, paratype) for x in ast.params]
        o += [Symbol(Function(),ast.name, MType(paratype, ast.return_type, ast.inherit))]
        return o

    def visitIntegerType(self, ast, param):
        return IntegerType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBooleanType(self, ast, param):
        return BooleanType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitAutoType(self, ast, param):
        return AutoType()

    def visitArrayType(self, ast, param):
        return ast


class ExpUtils:
    @staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntegerType, FloatType]

class StaticChecker(Visitor):
    # Global Environement - Built-in Functions - Default is Function
    global_envi = [
        Symbol(Function(),"readInteger", MType([], IntegerType())),
        Symbol(Function(),"printInteger", MType([IntegerType()], VoidType())),
        Symbol(Function(),"readFloat", MType([], FloatType())),
        Symbol(Function(),"writeFloat", MType([FloatType()], VoidType())),
        Symbol(Function(),"readBoolean", MType([], BooleanType())),
        Symbol(Function(),"printBoolean", MType([BooleanType()], VoidType())),
        Symbol(Function(),"readString", MType([], StringType())),
        Symbol(Function(),"printString", MType([StringType()], VoidType())),
        Symbol(Function(),"preventDefault", MType([], VoidType())),
        Symbol(Function(),"super", MType([], VoidType()))
    ]
    utils = Utils()
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, param):
        #env is first visit
        # data is list of Symbol
        env = GetEnv().visit(ast, None)
        param = {}
        param['first-visit'] = env

        ##add special function:
        param['special-func'] = self.global_envi
        #visit decls\
        param['global-scope'] = []
        for decl in ast.decls:
            if type(decl) is VarDecl:
                param['global-scope'] += [self.visit(decl,(param,True))]
            else:
                param = self.visit(decl,param)
                
        # no entry point
        entryPoint = Symbol(Function(),"main", MType([], VoidType()))
        flag = False
        for x in param['first-visit']:
            if x.name == 'main':
                if entryPoint.toTupleString() != x.toTupleString():
                    raise NoEntryPoint()
                else: flag = True
        if not flag: raise NoEntryPoint()
    
    def visitVarDecl(self, ast: VarDecl, param):
        # handle auto type
        env,isGlobal = param
        #check redeclared
        if isGlobal:
            for var in env['global-scope']:
                if var.name == ast.name:
                    raise Redeclared(Variable(),ast.name)
        else:
            for var in env[0]['local-variable']:
                if var.name == ast.name:
                    raise Redeclared(Variable(),ast.name)
            if len(env) == 2:
                for var in env[-1]['param-list']:
                    if var.name == ast.name:
                        raise Redeclared(Variable(),ast.name)
                for var in env[-1]['inherit']:
                    if var.name == ast.name:
                        raise Redeclared(Variable(),ast.name)   
        for x in self.global_envi:
            if x.name == ast.name: raise Redeclared(Variable(),ast.name)                    
        #find type of data init if exist
        if ast.init is not None: 
            type_init = self.visit(ast.init, env)     
        var_type = self.visit(ast.typ,env)
        
        #decl for an array
        if type(var_type) is ArrayType:  
            if type(var_type.typ) is AutoType:
                if ast.init is None:
                    raise Invalid(Variable(),ast.name)
                if type(type_init) is AutoType:
                    return Symbol(Variable(),ast.name,var_type,ast.init)
                var_type.typ = type_init.typ
            
            if ast.init is not None:
                if type(type_init) is AutoType:
                    # init data is auto type : array lit return auto type
                    for arr_lit in ast.init.explist:
                        if type(arr_lit) is FuncCall:
                            for x in env[-1]['first-vivit']:
                                if x.name == arr_lit.name:
                                    x.mtype.rettype = var_type.typ
                        else:
                            #set type for parameter of current function
                            for sym in env[-1]['first-visit']:
                                if sym.name ==  env[-1]['current-name']:
                                    for x in sym.mtype.partype:
                                        if x.name == arr_lit.name:
                                            x.mtype = var_type.typ
                                            return
                            # set type for parameter of parent function if exists       
                            if env[-1]['current-parent'] is not None:
                                for sym in env[-1]['first-visit']:
                                    if sym.name == env[-1]['current-parent']:
                                        for x in sym.mtype.partype:
                                            if x.name == arr_lit.name:
                                                x.mtype = var_type.typ   
                                                return                              
                # init data for array not auto type                                                        
                elif type(type_init.typ) is not type(var_type.typ):
                    if type(var_type.typ) is FloatType and  type(type_init) is IntegerType:
                        return Symbol(Variable(),ast.name,var_type,ast.init)
                    else: 
                        raise TypeMismatchInVarDecl(ast)
            #return new symbol  
            return Symbol(Variable(),ast.name,var_type,ast.init)                         
        #decl for an id
        else:
            if type(var_type) is AutoType:
                if ast.init is None:
                    raise Invalid(Variable(), ast.name)
                if type(type_init) is AutoType:
                    return Symbol(Variable(),ast.name,var_type,ast.init)
                var_type = type_init

            if ast.init is not None:
                if type(type_init) is AutoType:
                    # init is auto type
                    if type(ast.init) is FuncCall:
                        for x in env[-1]['first-visit']:
                            if x.name == ast.init.name:
                                x.mtype.rettype = var_type
                    else:
                        #set type for parameter of current function
                        for sym in env[-1]['first-visit']:
                            if sym.name ==  env[-1]['current-name']:
                                for x in sym.mtype.partype:
                                    if x.name == ast.init.name:
                                        if type(x.mtype) is ArrayType:
                                            x.mtype.typ = var_type
                                        else:
                                            x.mtype = var_type
                                        return Symbol(Variable(),ast.name,var_type,ast.init)
                        # set type for parameter of parent function if exists       
                        if env[-1]['current-parent'] is not None:
                            for sym in env[-1]['first-visit']:
                                if sym.name == env[-1]['current-parent']:
                                    for x in sym.mtype.partype:
                                        if type(x.mtype) is ArrayType:
                                            x.mtype.typ = var_type
                                        else:
                                            x.mtype = var_type   
                                        return Symbol(Variable(),ast.name,var_type,ast.init)

                elif type(type_init) is not type(var_type):
                    if type(ast.typ) is FloatType and  type(type_init) is IntegerType: 
                        return Symbol(Variable(),ast.name,var_type,ast.init)
                    else:
                        raise TypeMismatchInVarDecl(ast)  # vardecl not match with type of data init
            #return new symbol
            return Symbol(Variable(),ast.name,var_type,ast.init)

    def visitParamDecl(self, ast: ParamDecl, param):
        env, isinherit = param
        for x in self.global_envi:
            if x.name == ast.name: raise Redeclared(Parameter(),ast.name)   
        if isinherit:
            inherit_param = env['inherit']
            for x in inherit_param:
                if x.name == ast.name:
                    raise Invalid(Parameter(), ast.name)
        for x in env['param-list']:
            if x.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
        return Symbol(Parameter(),ast.name, self.visit(ast.typ,env), None, ast.inherit, ast.out)

    def visitFuncDecl(self, ast: FuncDecl, param):
        # param = {}
        # with param['first-visit'] = list of symbol after first vist
        # with param['global-scope'] = list of symbol of current visit
        env = param
        for x in param['global-scope']:
            if x.name == ast.name:
                raise Redeclared(Function(),ast.name)
            
        for x in self.global_envi:
            if x.name == ast.name: raise Redeclared(Function(),ast.name)          
        
        isinherit = False
        env['inherit'] = []
        if ast.inherit is not None:
            isinherit = True
            #parent function is declared
            flag = False
            for x in env['first-visit']:
                if x.name == ast.inherit:
                    flag = True
                    parent = x
            if not flag: raise Undeclared(Function(),ast.inherit)        
            
            inherit_para = []
            param_parent = []
            for param_func in parent.mtype.partype:
                if param_func.name not in param_parent:
                    param_parent += [param_func.name]
                else:
                    raise Redeclared(Parameter(),param.name)
                if param_func.inherit is True:
                    inherit_para += [param_func]
            env['inherit'] = inherit_para
        #visit param list
        env['param-list'] = []
        for x in ast.params:
            env['param-list'] += [self.visit(x, (env, isinherit))]

        env['current-name'] = ast.name
        env['current-rettype'] = ast.return_type
        env['first-return'] = False
        env['current-parent'] = ast.inherit
        # visit body, find return type
        self.visit(ast.body, (env, isinherit))
        #handel return type
        ## TO DO
        param['global-scope'] += [Symbol(Function(),ast.name,MType(env['param-list'],ast.return_type,ast.inherit))]
        return param
    # statements
    def visitAssignStmt(self, ast, param):
        env,inLoop,inStatement = param
        lhs = self.visit(ast.lhs, env)
        rhs = self.visit(ast.rhs, env)
        # not voidtype and arraytype
        if type(lhs) is VoidType or type(lhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if type(rhs) is VoidType or type(rhs) is ArrayType:
            raise TypeMismatchInStatement(ast)

        #handle auto type if exist
        if type(rhs) is AutoType and type(rhs) is type(lhs):
            return
        #rhs is auto type
        elif type(rhs) is AutoType:
            if type(ast.rhs) is FuncCall:
                for sym in env[-1]['first-visit']:
                    if sym.name == ast.rhs.name:
                        sym.mtype.rettype = lhs
                        rhs = lhs
                return
            else:
                #set type for parameter of current function
                for sym in env[-1]['first-visit']:
                    if sym.name ==  env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.rhs.name:
                                if type(x.mtype) is ArrayType:
                                    x.mtype.typ = lhs
                                else: 
                                    x.mtype = lhs
                                return
                 # set type for parameter of parent function if exists       
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                           for x in sym.mtype.partype:
                               if x.name == ast.rhs.name:
                                    if type(x.mtype) is ArrayType:
                                        x.mtype.typ = lhs
                                    else: 
                                        x.mtype = lhs   
                                    return  
        #lhs is auto type
        elif type(lhs) is AutoType:
                #set type for parameter of current function
            for sym in env[-1]['first-visit']:
                if sym.name ==  env[-1]['current-name']:
                    for x in sym.mtype.partype:
                        if x.name == ast.lhs.name:
                            if type(x.mtype) is ArrayType:
                                x.mtype.typ = rhs
                            else: 
                                x.mtype = rhs   
                            return  
                 # set type for parameter of parent function if exists       
            if env[-1]['current-parent'] is not None:
                for sym in env[-1]['first-visit']:
                    if sym.name == env[-1]['current-parent']:
                       for x in sym.mtype.partype:
                            if x.name == ast.lhs.name:
                                if type(x.mtype) is ArrayType:
                                    x.mtype.typ = rhs
                                else: 
                                    x.mtype = rhs   
                                return                  

        if (type(lhs) != type(rhs)):
            if type(lhs) is FloatType and type(rhs) is IntegerType:
                return
            else: raise TypeMismatchInStatement(ast)

    def visitBlockStmt(self, ast, param):
        # if function is children
        # handle first statement in body
        if len(param) == 3:
            #block stmt in block stmt
            env,inLoop,inStatement = param
            inStatement = True
            env = [{}] + env
            env[0]['local-variable'] = []
            for x in ast.body:
                if type(x) is VarDecl:
                    env[0]['local-variable'] += [self.visit(x, (env,False))]
                else:
                    self.visit(x, (env, inLoop,inStatement))
        else:
            env, isinherit = param
            env = [{}] + [env]
            env[0]['local-variable'] = []
            inLoop = False
            inStatement = False
            #if parent function is exist
            flag = False
            if isinherit:
                if len(ast.body) == 0: 
                    if len(env[-1]['inherit']) != 0:
                        raise TypeMismatchInExpression(None)
                    else: return
                if type(ast.body[0]) is not CallStmt:
                    #auto call super()
                    if len(env[-1]['inherit']) != 0:
                        raise TypeMismatchInExpression(None)
                else:
                    flag = True
                    if ast.body[0].name == 'super':
                        args = ast.body[0].args
                        inherit_list = env[-1]['inherit']
                        if len(args) != len(inherit_list):
                            if len(args) == 0: raise TypeMismatchInExpression([]) 
                            else : raise TypeMismatchInExpression(args[0]) 
                        else:
                            for count in range(len(args)):
                                expr_typ = self.visit(args[count],env)
                                if type(expr_typ) != type(inherit_list[count].mtype):
                                    if type(inherit_list[count].mtype) is AutoType:
                                        inherit_list[count].mtype = expr_typ
                                    elif type(inherit_list[count].mtype) is FloatType and type(expr_typ) is IntegerType:
                                        continue
                                    else: raise TypeMismatchInExpression(args[count])
                            
                    elif ast.body[0].name == 'preventDefault':
                        if len(ast.body[0].args) != 0:
                            raise TypeMismatchInExpression(ast.body[0].agrs[0])
                    else:
                        if env[-1]['inherit'] is not None:
                            raise TypeMismatchInExpression()
            #visit body
            for x in range(len(ast.body)):
                if x == 0 and flag == True:
                    continue
                if type(ast.body[x]) is VarDecl:
                    env[0]['local-variable'] += [self.visit(ast.body[x], (env,False))]
                else:
                    self.visit(ast.body[x], (env, inLoop,inStatement))

    def visitIfStmt(self, ast, param):
        env, inLoop,inStatement = param
        inStatement = True
        condexpr = self.visit(ast.cond, env)
        if type(condexpr) is not BooleanType:
            if type(condexpr) is AutoType:
                
                if type(ast.cond) is FuncCall:
                    for sym in env[-1]['first-visit']:
                        if sym.name == ast.cond.name:
                            sym.mtype.rettype = BooleanType()
                    return
                else:
                    #set type for parameter of current function
                    for sym in env[-1]['first-visit']:
                        if sym.name ==  env[-1]['current-name']:
                            for x in sym.mtype.partype:
                                if x.name == ast.cond.name:
                                    if type(x.mtype) is ArrayType:
                                        x.mtype.typ = BooleanType()
                                    else: 
                                        x.mtype = BooleanType()
                    # set type for parameter of parent function if exists       
                    if env[-1]['current-parent'] is not None:
                        for sym in env[-1]['first-visit']:
                            if sym.name == env[-1]['current-parent']:
                                for x in sym.mtype.partype:
                                    if x.name == ast.cond.name:
                                            if type(x.mtype) is ArrayType:
                                                x.mtype.typ = BooleanType()
                                            else: 
                                                x.mtype = BooleanType()                   
            else: 
                raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, (env, inLoop,inStatement))
        if ast.fstmt is not None: self.visit(ast.fstmt, (env, inLoop,inStatement))

    def visitForStmt(self, ast, param):
        env, inLoop,inStatement = param
        inLoop = True
        inStatement = True
        #scalar variable must be integer type
        scalarvar_typ = self.visit(ast.init.lhs,env)
        if type(scalarvar_typ) is not IntegerType:
            if type(scalarvar_typ) is AutoType:
                for sym in env[-1]['first-visit']:
                    if sym.name ==  env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.cond.name:
                                if type(x.mtype) is ArrayType:
                                    x.mtype.typ = IntegerType()
                                else: 
                                    x.mtype = IntegerType()
                    # set type for parameter of parent function if exists       
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                            for x in sym.mtype.partype:
                                if x.name == ast.cond.name:
                                    if type(x.mtype) is ArrayType:
                                            x.mtype.typ = IntegerType()
                                    else: 
                                        x.mtype = IntegerType() 
                # for x in env[-1]['param-list']:
                #     if x.name == ast.init.lhs.name:
                #         x.mtype = IntegerType()
                        
            else: raise TypeMismatchInStatement(ast)
        #visit init expr
        self.visit(ast.init,(env, inLoop, inStatement))
        
        condexpr = self.visit(ast.cond, env)
        if type(condexpr) is AutoType:
            if type(ast.cond) is FuncCall:
                for sym in env[-1]['first-visit']:
                    if sym.name == ast.cond.name:
                        sym.mtype.rettype = BooleanType()
            else:
                #set type for parameter of current function
                for sym in env[-1]['first-visit']:
                    if sym.name ==  env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.cond.name:
                                if type(x.mtype) is ArrayType:
                                    x.mtype.typ = BooleanType()
                                else: 
                                    x.mtype = BooleanType()
                 # set type for parameter of parent function if exists       
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                           for x in sym.mtype.partype:
                               if x.name == ast.cond.name:
                                    if type(x.mtype) is ArrayType:
                                        x.mtype.typ = BooleanType()
                                    else: 
                                        x.mtype = BooleanType()  
            condexpr = BooleanType() 
        if type(condexpr) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        updexpr = self.visit(ast.upd, env)
        if type(updexpr) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, (env, inLoop,inStatement))

    def visitWhileStmt(self, ast, param):
        env, inLoop,inStatement = param
        inLoop = True
        inStatement = True

        condexpr = self.visit(ast.cond, env)
        if type(condexpr) is AutoType:
            if type(ast.cond) is FuncCall:
                for sym in env[-1]['first-visit']:
                    if sym.name == ast.cond.name:
                        sym.mtype.rettype = BooleanType()
            else:
                #set type for parameter of current function
                for sym in env[-1]['first-visit']:
                    if sym.name ==  env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.cond.name:
                                if type(x.mtype) is ArrayType:
                                    x.mtype.typ = BooleanType()
                                else: 
                                    x.mtype = BooleanType()
                 # set type for parameter of parent function if exists       
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                           for x in sym.mtype.partype:
                               if x.name == ast.cond.name:
                                    if type(x.mtype) is ArrayType:
                                        x.mtype.typ = BooleanType()
                                    else: 
                                        x.mtype = BooleanType()  
            condexpr = BooleanType()
        if type(condexpr) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, (env, inLoop,inStatement))

    def visitDoWhileStmt(self, ast, param):
        env, inLoop, inStatement = param
        inLoop = True
        inStatement = True

        condexpr = self.visit(ast.cond, env)
        if type(condexpr) is AutoType:
            if type(ast.cond) is FuncCall:
                for sym in env[-1]['first-visit']:
                    if sym.name == ast.cond.name:
                        sym.mtype.rettype = BooleanType()
            else:
                #set type for parameter of current function
                for sym in env[-1]['first-visit']:
                    if sym.name ==  env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.cond.name:
                                if type(x.mtype) is ArrayType:
                                    x.mtype.typ = BooleanType()
                                else: 
                                    x.mtype = BooleanType()
                 # set type for parameter of parent function if exists       
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                           for x in sym.mtype.partype:
                               if x.name == ast.cond.name:
                                    if type(x.mtype) is ArrayType:
                                        x.mtype.typ = BooleanType()
                                    else: 
                                        x.mtype = BooleanType()  
            condexpr = BooleanType()
            
        if type(condexpr) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, (env, inLoop, inStatement))

    def visitBreakStmt(self, ast, param):
        env, inLoop,inStatement = param
        if not inLoop:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast, param):
        env, inLoop,inStatement = param
        if not inLoop:
            raise MustInLoop(ast)

    def visitReturnStmt(self, ast, param):
        env, inLoop,inStatement = param
        ##TO do
        # return in statement
        if inStatement or env[-1]['first-return'] is False:
            if env[-1]['first-return'] is False:
                env[-1]['first-return'] = True
            if ast.expr is not None:
                rettype = self.visit(ast.expr, env)
                #handle if return auto type
                if type(env[-1]['current-rettype']) is AutoType:
                    env[-1]['current-rettype'] = rettype
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-name']:
                            sym.mtype.rettype = rettype
                            
                if type(rettype) is AutoType:
                    rettype = env[-1]['current-rettype']
                    if type(ast.expr) is FuncCall:
                        for x in env[-1]['first-visit']:
                            if type(x.kind) is Function and x.name == ast.expr.name:
                                x.mtype.rettype = rettype
                    else:
                        for sym in env[-1]['first-visit']:
                            if sym.name ==  env[-1]['current-name']:
                                for x in sym.mtype.partype:
                                    if x.name == ast.expr.name:
                                        if type(x.mtype) is ArrayType:
                                            x.mtype.typ = rettype
                                        else: 
                                            x.mtype = rettype
                        # set type for parameter of parent function if exists       
                        if env[-1]['current-parent'] is not None:
                            for sym in env[-1]['first-visit']:
                                if sym.name == env[-1]['current-parent']:
                                    for x in sym.expr.partype:
                                        if x.name == ast.cond.name:
                                                if type(x.mtype) is ArrayType:
                                                    x.mtype.typ = rettype
                                                else: 
                                                    x.mtype = rettype                                 
                    return                   
                if type(rettype) != type(env[-1]['current-rettype']):
                    if type(env[-1]['current-rettype']) is FloatType and type(rettype) is IntegerType:
                        return
                    else: raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, param): 
        env,inLoop,inStatement = param
        flag = False
        if ast.name == 'super' or ast.name == 'preventDefault':
            raise InvalidStatementInFunction(ast.name)
        for ind in range(len(env)):
            if ind + 1 == len(env):
                break;
            else:
                for x in env[ind]['local-variable']:
                    if x.name == ast.name:
                        raise TypeMismatchInExpression(ast)  
        #args type
        for x in env[-1]['first-visit']:
            if x.name == ast.name and type(x.kind) is Function:
                flag = True
                rettype = x.mtype.rettype
                if type(rettype) is AutoType:
                    rettype = VoidType()
                    x.mtype.rettype = VoidType()
                arg_list = x.mtype.partype

        for x in env[-1]['special-func']:
            if type(x.kind) is Function and x.name == ast.name:
                flag = True
                arg_list = x.mtype.partype

        if not flag: raise Undeclared(Function(),ast.name)
        
        if len(arg_list) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        else:
            for x in range(len(ast.args)):
                arg_type = self.visit(ast.args[x],env)
                if type(arg_type) != type(arg_list[x].mtype if type(arg_list[x]) is Symbol else arg_list[x]):
                    if type(arg_type) is IntegerType and arg_list[x] is FloatType:
                        continue
                    raise TypeMismatchInStatement(ast)   
                 
    def visitBinExpr(self, ast, param):
        env = param
        e1t = self.visit(ast.left,param)
        e2t = self.visit(ast.right,param)
        #handle auto type
        # TO do
        if type(e1t) is type(e2t) and type(e1t) is AutoType:
            if type(ast.right) is FuncCall:
                for x in env[-1]['first-visit']:
                    if type(x.kind) is Function and x.name == ast.right.name:
                        if str(ast.op) in ['+', '-', '*', '/','%','<','>','<=','>=','==','!=']:
                            x.mtype.rettype = IntegerType()
                            e2t = IntegerType()
                        elif str(ast.op) in ['||', '&&']:
                            x.mtype.rettype = BooleanType()
                            e2t = BooleanType()
                        elif str(ast.op) in ['::']:
                            x.mtype.rettype = StringType()
                            e2t = StringType()
            else:
                for sym in env[-1]['first-visit']:
                    if sym.name ==  env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.right.name:
                                if type(x.mtype) is ArrayType:
                                    if str(ast.op) in ['+', '-', '*', '/','%','<','>','<=','>=','==','!=']:
                                        x.mtype.typ = IntegerType()
                                        e2t = IntegerType()
                                    elif str(ast.op) in ['||', '&&']:
                                        x.mtype.typ = BooleanType()
                                        e2t = BooleanType()
                                    elif str(ast.op) in ['::']:
                                        x.mtype.typ = StringType()
                                        e2t = StringType()
                                else: 
                                    if str(ast.op) in ['+', '-', '*', '/','%','<','>','<=','>=','==','!=']:
                                        x.mtype = IntegerType()
                                        e2t = IntegerType()
                                    elif str(ast.op) in ['||', '&&']:
                                        x.mtype = BooleanType()
                                        e2t = BooleanType()
                                    elif str(ast.op) in ['::']:
                                        x.mtype = StringType()   
                                        e2t = StringType()
                                        
                 # set type for parameter of parent function if exists       
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                           for x in sym.mtype.partype:
                               if x.name == ast.right.name:
                                    if type(x.mtype) is ArrayType:
                                        if str(ast.op) in ['+', '-', '*', '/','%','<','>','<=','>=','==','!=']:
                                            x.mtype.typ = IntegerType()
                                            e2t = IntegerType()
                                        elif str(ast.op) in ['||', '&&']:
                                            x.mtype.typ = BooleanType()
                                            e2t = BooleanType()
                                        elif str(ast.op) in ['::']:
                                            x.mtype.typ = StringType()
                                            e2t = StringType()
                                    else: 
                                        if str(ast.op) in ['+', '-', '*', '/','%','<','>','<=','>=','==','!=']:
                                            x.mtype = IntegerType()
                                            e2t = IntegerType()
                                        elif str(ast.op) in ['||', '&&']:
                                            x.mtype = BooleanType()
                                            e2t = BooleanType()
                                        elif str(ast.op) in ['::']:
                                            x.mtype = StringType()   
                                            e2t = StringType()                              
        if type(e1t) is AutoType:
            if type(ast.left) is FuncCall:
                for x in env[-1]['first-visit']:
                    if type(x.kind) is Function and x.name == ast.left.name:
                        x.mtype.rettype = e2t
                        e1t = e2t
            else:
                #param í auto type
                for sym in env[-1]['first-visit']:
                    if sym.name == env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.left.name:
                                if type(x.mtype) is ArrayType:
                                    x.mtype.typ = e2t
                                    e1t = e2t
                                else: 
                                    x.mtype = e2t
                                    e1t = e2t
                #param of inherit is auto typ
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                            for x in sym.mtype.partype:
                                if x.name == ast.left.name:
                                    if type(x.mtype) is ArrayType:
                                        x.mtype.typ = e2t
                                        e1t = e2t
                                    else: 
                                        x.mtype = e2t
                                        e1t = e2t        
            return e2t
        
        elif type(e2t) is AutoType:
            if type(ast.right) is FuncCall:
                for x in env[-1]['first-visit']:
                    if type(x.kind) is Function and x.name == ast.right.name:
                        x.mtype.rettype = e1t
                        e2t = e1t
            else:
                for sym in env[-1]['first-visit']:
                    if sym.name == env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.right.name:
                                if type(x.mtype) is ArrayType:
                                    x.mtype.typ = e1t
                                    e2t = e1t
                                else: 
                                    x.mtype = e1t
                                    e2t = e1t
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                            for x in sym.mtype.partype:
                                if x.name == ast.left.name:
                                    if type(x.mtype) is ArrayType:
                                        x.mtype.typ = e2t
                                        e1t = e2t
                                    else: 
                                        x.mtype = e2t
                                        e1t = e2t    
            return e1t

        # both of expressions not autotype
        if str(ast.op) in ['+', '-', '*']:
            if ExpUtils.isNaNType(e1t) or ExpUtils.isNaNType(e2t):
                raise TypeMismatchInExpression(ast)
            if type(e1t) is FloatType or type(e2t) is FloatType:
                return FloatType()
            return IntegerType()
        if str(ast.op) in ['/']:
            if ExpUtils.isNaNType(e1t) or ExpUtils.isNaNType(e2t):
                raise TypeMismatchInExpression(ast)
            return FloatType()
        if str(ast.op) in ['%']:
            if type(e1t) is not IntegerType or type(e2t) is not IntegerType:
                raise TypeMismatchInExpression(ast)
            return IntegerType()
        if str(ast.op) in ['||', '&&']:
            if type(e1t) is not BooleanType or type(e2t) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if str(ast.op) in ['::']:
            if type(e1t) is not StringType or type(e2t) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        if str(ast.op) in ['==', '!=']:
            if type(e1t) is type(e2t) :
                if type(e1t) is IntegerType or type(e1t) is BooleanType:
                    return BooleanType()
            raise TypeMismatchInExpression(ast)
        if str(ast.op) in ['<', '<=', '>', '>=']:
            if ExpUtils.isNaNType(e1t) or ExpUtils.isNaNType(e2t):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

    def visitUnExpr(self, ast, param):
        env = param
        expr = self.visit(ast.val,param)
        if type(expr) is AutoType:
            
            if type(ast.val) is FuncCall:
                for sym in env[-1]['first-visit']:
                    if sym.name == ast.val.name:
                        if str(ast.op) == '!':
                            sym.mtype.rettype = BooleanType()
                            return BooleanType()    
                        else: 
                            sym.mtype.rettype = IntegerType()
                            return IntegerType()
            else:
                #set type for parameter of current function
                for sym in env[-1]['first-visit']:
                    if sym.name ==  env[-1]['current-name']:
                        for x in sym.mtype.partype:
                            if x.name == ast.val.name:
                                if type(x.mtype) is ArrayType:
                                    if str(ast.op) == '!':
                                        x.mtype.typ = BooleanType()
                                        return BooleanType()    
                                    else: 
                                        x.mtype.typ = IntegerType()
                                        return IntegerType()
                                else: 
                                    if str(ast.op) == '!':
                                        x.mtype = BooleanType()
                                        return BooleanType()    
                                    else: 
                                        x.mtype = IntegerType()
                                        return IntegerType()
                 # set type for parameter of parent function if exists       
                if env[-1]['current-parent'] is not None:
                    for sym in env[-1]['first-visit']:
                        if sym.name == env[-1]['current-parent']:
                           for x in sym.mtype.partype:
                               if x.name == ast.val.name:
                                    if type(x.mtype) is ArrayType:
                                        if str(ast.op) == '!':
                                            x.mtype.typ = BooleanType()
                                            return BooleanType()    
                                        else: 
                                            x.mtype.typ = IntegerType()
                                            return IntegerType()
                                    else: 
                                        if str(ast.op) == '!':
                                            x.mtype = BooleanType()
                                            return BooleanType()    
                                        else: 
                                            x.mtype = IntegerType()
                                            return IntegerType()
            
        if (str(ast.op) == '-' and ExpUtils.isNaNType(expr)) or (str(ast.op) == '!' and type(expr) is not BooleanType):
            raise TypeMismatchInExpression(ast)
        return expr

    def visitId(self, ast, param):
        env = param
        for ind in range(len(env)):
            if ind + 1 == len(env):
                break;
            else:
                for x in env[ind]['local-variable']:
                    if x.name == ast.name:
                        return x.mtype
        for sym in env[-1]['first-visit']:
            if sym.name ==  env[-1]['current-name']:
                for x in sym.mtype.partype:
                    if x.name == ast.name:
                        return x.mtype
                 # set type for parameter of parent function if exists       
        if env[-1]['current-parent'] is not None:
            for sym in env[-1]['first-visit']:
                if sym.name == env[-1]['current-parent']:
                    for x in sym.mtype.partype:
                        if x.name == ast.name:
                            return x.mtype 
                        
        for x in env[-1]['global-scope']:
            if type(x.kind) is Variable and x.name == ast.name:
                return x.mtype
            
        raise Undeclared(Variable(),ast.name)

    def visitArrayCell(self, ast, param):
        env= param
        flag = False
        
        arr_type = self.visit(Id(ast.name),env)
        if type(arr_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        cell = ast.cell
        dimension = arr_type.dimensions
        if len(cell) != len(dimension):
            raise TypeMismatchInExpression(ast)
        else:
            for expr in ast.cell:
                typ = self.visit(expr,env)
                if type(typ) is not IntegerType:
                    raise TypeMismatchInExpression(ast)
        return arr_type.typ

    def visitIntegerLit(self, ast, param):
        return IntegerType()

    def visitFloatLit(self, ast, param):
        return FloatType()

    def visitStringLit(self, ast, param):
        return StringType()

    def visitBooleanLit(self, ast, param):
        return BooleanType()

    def visitArrayLit(self, ast, param):
        ### to do 
        env = param
        for array_lit in ast.explist:
            arr_typ = self.visit(array_lit,param)
            if type(arr_typ) is not AutoType:
                break;
        
        for array_lit in ast.explist:
            typ = self.visit(array_lit,param)
            #if datalit is auto type
            if type(typ) is AutoType:
                #set type for parameter of current function
                if type(array_lit) is FuncCall:
                    for x in env[-1]['first-visit']:
                        if x.name == array_lit.name:
                            x.mtype.rettype = arr_typ
                else: 
                    for sym in env[-1]['first-visit']:
                        if sym.name ==  env[-1]['current-name']:
                            for x in sym.mtype.partype:
                                if x.name == array_lit.name:
                                    x.mtype = arr_typ
                                    typ = arr_typ
                    # set type for parameter of parent function if exists       
                    if env[-1]['current-parent'] is not None:
                        for sym in env[-1]['first-visit']:
                            if sym.name == env[-1]['current-parent']:
                                for x in sym.mtype.partype:
                                    if x.name == array_lit.name:
                                        x.mtype = arr_typ
                                        typ = arr_typ
            if type(typ) != type(arr_typ):
                if type(arr_typ) is FloatType and type(typ) is IntegerType:
                    continue
                elif type(typ) is FloatType and type(arr_typ) is IntegerType:
                    arr_typ = typ
                    continue
                else: raise IllegalArrayLiteral(ast)
            
        return ArrayType(len(ast.explist),arr_typ)

    def visitFuncCall(self, ast, param):
        env = param
        flag = False
        if ast.name == 'super' or ast.name == 'preventDefault':
            raise InvalidStatementInFunction(ast.name)
        for ind in range(len(env)):
            if ind + 1 == len(env):
                break;
            else:
                for x in env[ind]['local-variable']:
                    if x.name == ast.name:
                        raise TypeMismatchInExpression(ast)        
        
        for x in env[-1]['first-visit']:
            if x.name == ast.name and type(x.kind) is Function:
                flag = True
                rettype = x.mtype.rettype
                arg_list = x.mtype.partype

        for x in env[-1]['special-func']:
            if x.name == ast.name and type(x.kind) is Function:
                flag = True
                rettype = x.mtype.rettype
                arg_list = x.mtype.partype

        if not flag: raise Undeclared(Function(),ast.name)
        if len(ast.args) != len(arg_list):
            raise TypeMismatchInExpression(ast)
        else:
            for x in range(len(ast.args)):
                arg_type = self.visit(ast.args[x],env)
                if type(arg_type) != type(arg_list[x].mtype if type(arg_list[x]) is Symbol else arg_list[x]):
                    if type(arg_type) is IntegerType and arg_list[x] is FloatType:
                        continue
                    raise TypeMismatchInExpression(ast)
        return rettype
    def visitIntegerType(self, ast, param):
        return IntegerType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBooleanType(self, ast, param):
        return BooleanType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ast

    def visitAutoType(self, ast, param):
        return AutoType()

    def visitVoidType(self, ast, param):
        return VoidType()
