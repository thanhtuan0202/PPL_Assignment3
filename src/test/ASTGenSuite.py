import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_vardecl_1(self):
        input = """x, y, z: integer;"""
        expect = str(Program([VarDecl("x", IntegerType()),VarDecl("y", IntegerType()),VarDecl("z", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_vardecl_2(self):
        input = """x,y,z: integer = 1,2,3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecl_3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float= x,y;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType, Id(x))
	VarDecl(b, FloatType, Id(y))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_vardecl_4(self):
        input = """
        main: function void(){
                a,b,c : float ;
                c,d,e,f : boolean = true,true,false,false;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, FloatType), VarDecl(c, BooleanType, BooleanLit(True)), VarDecl(d, BooleanType, BooleanLit(True)), VarDecl(e, BooleanType, BooleanLit(True)), VarDecl(f, BooleanType, BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))
        
    def test_vardecl_5(self):
        input = """a,b,c : float ;
        main: function void(){
                c,d,e,f : boolean = true,true,false,false;
            }
        """
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(c, BooleanType, BooleanLit(True)), VarDecl(d, BooleanType, BooleanLit(True)), VarDecl(e, BooleanType, BooleanLit(True)), VarDecl(f, BooleanType, BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))      
        
    def test_func_1(self):
        input = """
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    def test_func_2(self):
        input = """
        main: function void () {
            printInteger(4);
        }"""    
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    def test_func_3(self):
        input = """
        foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
        main: function void () {
            printInteger(4);
        }"""    
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    def test_func_4(self):
        input = """
        foo: function integer (a: integer,b: integer){return a + b;}
        main: function void () {
            printInteger(4);
        }"""    
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_func_5(self):
        input = """
        foo: function integer (out a: integer,out b: integer){return a + b;}
        main: function void () {
            printInteger(4);
        }"""    
        expect = """Program([
	FuncDecl(foo, IntegerType, [OutParam(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
       
    def test_assign_1(self):
        input = """foo: function void(a:integer, b: integer){
            x,y : integer;
            x = a;
            y= b;
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), AssignStmt(Id(x), Id(a)), AssignStmt(Id(y), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    def test_assign_2(self):
        input = """foo: function void(a: integer){
            arr[1] = a;
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(1)]), Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_assign_3(self):
        input = """foo: function void(a:integer, b: integer){
            arr : array [1] of integer = {};
            a[0] = a+ b;
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([VarDecl(arr, ArrayType([1], IntegerType), ArrayLit([])), AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    def test_assign_4(self):
        input = """
        main: function void(){
            a : integer;
            a = -(3 + 4) * 5; 
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(*, UnExpr(-, BinExpr(+, IntegerLit(3), IntegerLit(4))), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    def test_assign_5(self):
        input = """
        main: function void(){
            a : integer;
            a = -3 + 4  * 5; 
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(+, UnExpr(-, IntegerLit(3)), BinExpr(*, IntegerLit(4), IntegerLit(5))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
    def test_assign_6(self):
        input = """
        main: function void(){
            a : integer;
            a = -(3 + 4) * 5; 
            arr : array [1,2] of integer = {};
            arr[0,0] = a;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(*, UnExpr(-, BinExpr(+, IntegerLit(3), IntegerLit(4))), IntegerLit(5))), VarDecl(arr, ArrayType([1, 2], IntegerType), ArrayLit([])), AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]), Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    def test_assign_7(self):
        input = """
        foo: function integer (out a: integer,out b: integer){return a + b;}
        main: function void () {
            a : integer ;
            a = foo(2,3);
        }"""    
        expect = """Program([
	FuncDecl(foo, IntegerType, [OutParam(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), FuncCall(foo, [IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    def test_array_assign_8(self):
        input = """foo: function void(arr : array [1] of float,a :integer, a : array [1] of integer){
                //do something
            }
            """
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(arr, ArrayType([1], FloatType)), Param(a, IntegerType), Param(a, ArrayType([1], IntegerType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,325))
    def test_array_assign_9(self):
        input = """foo: function void(arr : array [1] of float){
                //do something
            }
            """
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(arr, ArrayType([1], FloatType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,326))
    def test_array_assign_10(self):
        input = """foo: function void(arr : array [1] of float, a : float){
                //do something
            }
            main: function void(){
                arr : array [1] of float;
                foo(arr,arr[0]);
            }
            """
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(arr, ArrayType([1], FloatType)), Param(a, FloatType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([1], FloatType)), CallStmt(foo, Id(arr), ArrayCell(arr, [IntegerLit(0)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,327))


    def test_if_statement1(self):
        input = """foo: function void(a : integer,b :integer){
            if(a > 1){
                b = b *2;
            }
        }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_if_statement2(self):
        input = """foo: function void(a : integer,b :integer){
            if(a > 1){
                b = b *2;
            }else b = b + 1;
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2)))]), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    def test_if_statement3(self):
        input = """foo: function void(a : integer,b :integer){
            if(a > 1) for(i = 1,i < 4,i+1){
                if(a == 0){b = b + 1;}
                else b = b  + 4;
                b = b *2;
            }
            else {if(a == 0){
                b = b * b;
            }
           }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))]), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(4)))), AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2)))])), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(b), BinExpr(*, Id(b), Id(b)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
    def test_if_statement4(self):
        input = """foo: function void(a : integer,b :integer){
            if(a > 1){
                b = b *2;
            }else foo(a + 1,b);
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2)))]), CallStmt(foo, BinExpr(+, Id(a), IntegerLit(1)), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    def test_if_statement6(self):
        input = """foo: function void(a : integer,b :integer){
            if(a > 1){
                b = b *2;
            }
            else {}
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2)))]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test_while_1(self):
        input = """foo: function void(a : integer, out b : integer){
                while(a >= 1){
                    b = b * 2;
                    a = a+ 1;
                }
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2))), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,322))
    def test_while_2(self):
        input = """foo: function void(a : integer, out b : integer){
                while(a >= 1){
                    if(b  % 2 == 1) b = b * b;
                    a = a + 1;
                }
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(b), IntegerLit(2)), IntegerLit(1)), AssignStmt(Id(b), BinExpr(*, Id(b), Id(b)))), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,323))
    def test_while_3(self):
        input = """foo: function void(a : integer, out b : integer){
                while(a >= 10){
                    if(b % 2 == 1) b = b * 2;
                    else b = b + 1;
                    a = a+ 1;
                }
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(b), IntegerLit(2)), IntegerLit(1)), AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2))), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,324))
        
    def test_call_1(self):
        input = """foo: function void(a : integer){
            i : integer;
              for(i =0,i < a,i +1){
                  writeinteger(i);
              }
            }
            main:function void(){
                a : integer = 3;
                foo(3);    
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(a)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeinteger, Id(i))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(3)), CallStmt(foo, IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input,expect,328))

    def test_for_statement1(self):
        input = """foo: function void(a : integer, out b : integer){
                i : integer = 0;
               for(i = 0, i < 10,i+1){
                   writeinteger(i);
               }
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeinteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,329))
        
    # 
    #30-39
    #
    def test_string(self):
        input = """a :string  = "hello world!";"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(hello world!))
])"""
        self.assertTrue(TestAST.test(input,expect,330))
    def test_string_1(self):
        input = """
        a :string  = "hello world!";
        b : string = "who am i?";
        """
        expect = """Program([
	VarDecl(a, StringType, StringLit(hello world!))
	VarDecl(b, StringType, StringLit(who am i?))
])"""
        self.assertTrue(TestAST.test(input,expect,331))
    def test_string_2(self):
        input = """
        a,b :string  = "hello world!","who am i?";
        """
        expect = """Program([
	VarDecl(a, StringType, StringLit(hello world!))
	VarDecl(b, StringType, StringLit(who am i?))
])"""
        self.assertTrue(TestAST.test(input,expect,332))
    def test_string_3(self):
        input = """
        a :string  = "hello world!";
        b : string = "who am i?";
        main: function void(){
            c : string = a :: b;
            printString(i);
        }
        """
        expect = """Program([
	VarDecl(a, StringType, StringLit(hello world!))
	VarDecl(b, StringType, StringLit(who am i?))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(c, StringType, BinExpr(::, Id(a), Id(b))), CallStmt(printString, Id(i))]))
])"""
        self.assertTrue(TestAST.test(input,expect,333))    
    def test_string_4(self):
        input = """
        main: function void(){
            c : string;
            do{
                c = readString();
                if(c[0] <= c[1]){
                    if(c[1] <= c[2]){
                        printString("true");
                    }
                }
                printString("false");
            }
            while(s != "***");
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(c, StringType), DoWhileStmt(BinExpr(!=, Id(s), StringLit(***)), BlockStmt([AssignStmt(Id(c), FuncCall(readString, [])), IfStmt(BinExpr(<=, ArrayCell(c, [IntegerLit(0)]), ArrayCell(c, [IntegerLit(1)])), BlockStmt([IfStmt(BinExpr(<=, ArrayCell(c, [IntegerLit(1)]), ArrayCell(c, [IntegerLit(2)])), BlockStmt([CallStmt(printString, StringLit(true))]))])), CallStmt(printString, StringLit(false))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,334))       
    def test_string_5(self):
        input = """
        main: function void(){
            s : string = "kadfkdfkakfdkf";
            printSting(s);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType, StringLit(kadfkdfkakfdkf)), CallStmt(printSting, Id(s))]))
])""";
        self.assertTrue(TestAST.test(input,expect,335))
    def test_string_6(self):
        input = """
        main: function void(){
            s : string;
            s = readString();  
            ans : integer = 1;
            start : integer = 0;
            s = s + "*";
            i : integer;
            for (i = 0, i < length(s), i+1)
                if (s[i] != s[i + 1]) {
                    ans = max(ans, i + 1 - start);
                    start = i + 1;
                }
            printInteger(ans); 
        }""";
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType), AssignStmt(Id(s), FuncCall(readString, [])), VarDecl(ans, IntegerType, IntegerLit(1)), VarDecl(start, IntegerType, IntegerLit(0)), AssignStmt(Id(s), BinExpr(+, Id(s), StringLit(*))), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(s)])), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(!=, ArrayCell(s, [Id(i)]), ArrayCell(s, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([AssignStmt(Id(ans), FuncCall(max, [Id(ans), BinExpr(-, BinExpr(+, Id(i), IntegerLit(1)), Id(start))])), AssignStmt(Id(start), BinExpr(+, Id(i), IntegerLit(1)))]))), CallStmt(printInteger, Id(ans))]))
])""";
        self.assertTrue(TestAST.test(input,expect,336))
    def test_string_7(self):
        input = """
        main: function void(){
            s : string = "dndhjdsfjdsjfsdifidsf112923f";
            printSting(s);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType, StringLit(dndhjdsfjdsjfsdifidsf112923f)), CallStmt(printSting, Id(s))]))
])"""
        self.assertTrue(TestAST.test(input,expect,337))
    def test_string_8(self):
        input = """
        main: function void(){
            s : string = "u1823213hjwhuafna0-1@(!11)";
            printSting(s);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType, StringLit(u1823213hjwhuafna0-1@(!11))), CallStmt(printSting, Id(s))]))
])"""
        self.assertTrue(TestAST.test(input,expect,338))   
  
    def test_for_statement2(self):
        input = """foo: function void(a : integer, out b : integer){
                i : integer = 0;
               for(i = 0, i < 10,i+1){
                   if( i % 2 == 0) b = b * 2;
               }
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2))))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,340))
    def test_for_statement3(self):
        input = """foo: function void(a : integer, out b : integer){
                i : integer = 0;
                j : integer = 0;
               for(i = 0, i < 10,i+1){
                   for(j = 0, j < i,j + 1){
                       //do something in here
                   }
               }
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,341))

    def test_break_statement(self):
        input = """foo: function void(a : integer){
                i : integer = 0;
               for(i = 0, i < 10,i+1){
                   if(i == a) break;
                   writeinteger(i);
               }
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), Id(a)), BreakStmt()), CallStmt(writeinteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,342))
    def test_continue_statement(self):
        input = """foo: function void(a : integer, out b : integer){
                i : integer = 0;
               while(true){
                   continue;
               }
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BooleanLit(True), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,343))
    #random function
    def test_random_1(self):
        input = """foo: function array [2] of float(a : integer){
                a : array [2] of float;
                a[0] = a * 3.14;
                a[1] = a * a * 3.14;
                return a;
            }"""
        expect = """Program([
	FuncDecl(foo, ArrayType([2], FloatType), [Param(a, IntegerType)], None, BlockStmt([VarDecl(a, ArrayType([2], FloatType)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(*, Id(a), FloatLit(3.14))), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(*, BinExpr(*, Id(a), Id(a)), FloatLit(3.14))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input,expect,344))
        
    def test_radom_2(self):
        input = """
        fib: function integer(n : integer){
            if(n == 0) return 0;
            else if (n == 1) return 1;
            return fib(n - 1) + fib(n - 2);
        }
        main: function void(){
            n : integer = 9;
            fib(n);
        }
        """
        expect = """Program([
	FuncDecl(fib, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(0)), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1)))), ReturnStmt(BinExpr(+, FuncCall(fib, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fib, [BinExpr(-, Id(n), IntegerLit(2))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(9)), CallStmt(fib, Id(n))]))
])"""
        self.assertTrue(TestAST.test(input,expect,345))  
        
    def test_random_3(self):
        input = """
        fib: function integer(n : integer){
            a,b,c : integer = 0,1,1;
            i : integer;
            if(n == 0) return 0;
            for(i = 2, i <= n,i+1){
                c = a +b;
                a =b;
                b=c;
            }
            return b;
        }
        main:function void(){
            n : integer = 9;
            printInteger(fib(9));
        }
        """
        expect = """Program([
	FuncDecl(fib, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(1)), VarDecl(c, IntegerType, IntegerLit(1)), VarDecl(i, IntegerType), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(a), Id(b))), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(c))])), ReturnStmt(Id(b))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(9)), CallStmt(printInteger, FuncCall(fib, [IntegerLit(9)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,346))
    def test_random_4(self):
        input = """
        reverse: function void (out arr : array [4] of integer){
            tmp : integer;
            for(i = 0, i < 2,i+1){
                tmp = arr[i];
                arr[i] = arr[3-i];
                arr[3-i] = tmp;
            }
        }
        main: function void(){
            arr : array [4] of integer = {1,2,3,4};
            reverse(arr);
            for(i = 0, i < 4,i +1){
                printInteger(arr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(reverse, VoidType, [OutParam(arr, ArrayType([4], IntegerType))], None, BlockStmt([VarDecl(tmp, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(tmp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(-, IntegerLit(3), Id(i))])), AssignStmt(ArrayCell(arr, [BinExpr(-, IntegerLit(3), Id(i))]), Id(tmp))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(reverse, Id(arr)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(arr, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,347))
    def test_random_5(self):
        input = """
        swap:function void(out a: integer,out b: integer){
                tmp = a;
                a = b;
               b = tmp;
        }
        sapxep: function void (out arr : array [4] of integer){
            tmp : integer;
            for(i = 0, i < 4,i+1){
                for(j = i , j < 4,j+1){
                    if(arr[i] > arr[j]) swap(arr[j],arr[i]);
                }
            }
        }
        main: function void(){
            arr : array [4] of integer = {1,3,7,4};
            sapxep(arr);
            for(i = 0, i < 4,i +1){
                printInteger(arr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(swap, VoidType, [OutParam(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([AssignStmt(Id(tmp), Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(tmp))]))
	FuncDecl(sapxep, VoidType, [OutParam(arr, ArrayType([4], IntegerType))], None, BlockStmt([VarDecl(tmp, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), Id(i)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), CallStmt(swap, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [Id(i)])))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(4)])), CallStmt(sapxep, Id(arr)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(arr, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,348))
    def test_random_6(self):
        input = """
        sum: function integer (out arr : array [4] of integer){
            sum : integer = 0;
            for(i = 0, i < 2,i+1){
                sum = sum + arr[i];
            }
            return sum;
        }
        main: function void(){
            arr : array [4] of integer = {1,2,3,4};
            sum(arr);
            printInteger(arr[i]);
        }"""
        expect = """Program([
	FuncDecl(sum, IntegerType, [OutParam(arr, ArrayType([4], IntegerType))], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(sum, Id(arr)), CallStmt(printInteger, ArrayCell(arr, [Id(i)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,349))
    def test_random_7(self):
        input = """
        luythua: function integer(n : integer, x : integer){
            if(n == 1) return x;
            return x * luythua(n-1,x);
        }
        main: function void(){
            x = readInteger();
            n = readInteger();
            printInteger(luythua(n,x));
        }
        """
        expect = """Program([
	FuncDecl(luythua, IntegerType, [Param(n, IntegerType), Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(Id(x))), ReturnStmt(BinExpr(*, Id(x), FuncCall(luythua, [BinExpr(-, Id(n), IntegerLit(1)), Id(x)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), FuncCall(readInteger, [])), AssignStmt(Id(n), FuncCall(readInteger, [])), CallStmt(printInteger, FuncCall(luythua, [Id(n), Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,350))
    def test_random_8(self):
        input = """
        main: function void(){
            n : integer;
            i: integer = 0;
            sum : float = 0.0;
            n = readInteger();
            while(i < n){
                sum = sum + 1 / i;
                i = i + 1;
            }
            writeFloat(sum);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(sum, FloatType, FloatLit(0.0)), AssignStmt(Id(n), FuncCall(readInteger, [])), WhileStmt(BinExpr(<, Id(i), Id(n)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), BinExpr(/, IntegerLit(1), Id(i)))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), CallStmt(writeFloat, Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input,expect,351))
    def test_random_9(self):
        input = """a: array[5] of integer = {1, 2, 3, 4, 5};
                func: function integer(low: integer, high: integer) {
                    if ((low < 0) || (high < 0) || (low >= 5) || (high >= 5))
                        return -1;
    
                    sum = 0;
                    for (i = low, i <= high, i+1)
                        sum = sum + a[i];
                    return sum;
                }
        """
        expect = """Program([
	VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(func, IntegerType, [Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(<, Id(low), IntegerLit(0)), BinExpr(<, Id(high), IntegerLit(0))), BinExpr(>=, Id(low), IntegerLit(5))), BinExpr(>=, Id(high), IntegerLit(5))), ReturnStmt(UnExpr(-, IntegerLit(1)))), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), Id(low)), BinExpr(<=, Id(i), Id(high)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(a, [Id(i)])))), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input,expect,352))
    def test_random_10(self):
        input = """func: function integer(n: integer) {
                    i = 1;
                    product = 1;
                    while (i <= n) {
                        product = product * i;
                        i = i + 1;
                    }
                    return product;
                }
            """
        expect = """Program([
	FuncDecl(func, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(i), IntegerLit(1)), AssignStmt(Id(product), IntegerLit(1)), WhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([AssignStmt(Id(product), BinExpr(*, Id(product), Id(i))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(product))]))
])"""
        self.assertTrue(TestAST.test(input,expect,353))
    def test_random_11(self):
        input = """func: function void() {
            a = 2;
            b = 3;
            if (a > b) {
                writeString("a is greater than b");
            } else if (a < b) {
                writeString("a is less than b");
            } else {
                writeString("a is equal to b");
            }
        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), IntegerLit(3)), IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([CallStmt(writeString, StringLit(a is greater than b))]), IfStmt(BinExpr(<, Id(a), Id(b)), BlockStmt([CallStmt(writeString, StringLit(a is less than b))]), BlockStmt([CallStmt(writeString, StringLit(a is equal to b))])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,354))
    def test_random_12(self):
        input = """func: function integer(a: integer, b: integer) {
            if (a == 0) {
                return b;
            }
            while (b != 0) {
                if (a > b) {
                    a = a - b;
                } else {
                    b = b - a;
                }
            }
            return a;
        }
        main: function void(){
            a,b : integer;
            a = readInteger();
            b = readInteger();
            max = func(a,b);
            printInteger(max);
        }
        """
        expect = """Program([
	FuncDecl(func, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([ReturnStmt(Id(b))])), WhileStmt(BinExpr(!=, Id(b), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), Id(b)))]), BlockStmt([AssignStmt(Id(b), BinExpr(-, Id(b), Id(a)))]))])), ReturnStmt(Id(a))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), AssignStmt(Id(a), FuncCall(readInteger, [])), AssignStmt(Id(b), FuncCall(readInteger, [])), AssignStmt(Id(max), FuncCall(func, [Id(a), Id(b)])), CallStmt(printInteger, Id(max))]))
])"""
        self.assertTrue(TestAST.test(input,expect,355))
    def test_random_13(self):
        input = """
        main: function void() {
            x: array[3,3] of integer= {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
            for (i = 0, i < 3,i + 1) {
                for (j = 0, j < 3,j + 1) {
                    writeInt(x[i,j]);
                }
                writeLn();
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(writeInt, ArrayCell(x, [Id(i), Id(j)]))])), CallStmt(writeLn, )]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,356))
    def test_random_14(self):
        input = """
        main : function void(){
            i : integer;
            i = readInteger();
            if (i % 2 == 0) {
                writeString("even");
            } else {
                writeString("odd");
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), AssignStmt(Id(i), FuncCall(readInteger, [])), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(writeString, StringLit(even))]), BlockStmt([CallStmt(writeString, StringLit(odd))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,357))
    def test_random_15(self):
        input = """
        iseven: function boolean(a : integer){
            if (a % 2 == 0) return true;
            return false;
        }
        main : function void(){
            i : integer;
            i = readInteger();
            writeString("Is i even number?");
            printBoolean(iseven(i));
        }
        """
        expect = """Program([
	FuncDecl(iseven, BooleanType, [Param(a, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), ReturnStmt(BooleanLit(True))), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), AssignStmt(Id(i), FuncCall(readInteger, [])), CallStmt(writeString, StringLit(Is i even number?)), CallStmt(printBoolean, FuncCall(iseven, [Id(i)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,358))
    def test_random_16(self):
        input = """main:function void(){
        a : integer;
        a=10;
        while (a<20)
            writeln(a);
            a=a+1;
            if (a == 15)
                break;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), IntegerLit(10)), WhileStmt(BinExpr(<, Id(a), IntegerLit(20)), CallStmt(writeln, Id(a))), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(15)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input,expect,359))
    def test_random_17(self):
        input = """main:function void(){
        a : integer;
        a=10;
        while (a<20){
            writeln(a);
            a=a+1;
            if (a == 15) continue;
        }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), IntegerLit(10)), WhileStmt(BinExpr(<, Id(a), IntegerLit(20)), BlockStmt([CallStmt(writeln, Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(15)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,360))
    def test_random_18(self):
        input = """func: function void() {
                for (i = 0, i < 10, 1) {
                    for (j = 0, j < 10, 1) {
                        if (i + j == 10) {
                            continue;
                        }
                        writeInt(i);
                        writeInt(j);
                    }
                }
            }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), IntegerLit(1), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(i), Id(j)), IntegerLit(10)), BlockStmt([ContinueStmt()])), CallStmt(writeInt, Id(i)), CallStmt(writeInt, Id(j))]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,361))
    def test_random_19(self):
        input = """main:function void(){
            counter : integer = 0;
            i,j : integer;
            arr : array [4,4] of integer;
            for(i = 0,i < 4,i+1){
                for(j = 0,j < 4,j+1){
                    arr[i,j] = readInteger();
                    if( arr[i,j] == 0) {counter = counter + 1;}
                }
            }
            if(counter > (16 - counter)) {
                printString("The entered matrix is a sparse matrix");
            }
            else printString("The entered matrix is not a sparse matrix");   
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(counter, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(arr, ArrayType([4, 4], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), Id(j)]), FuncCall(readInteger, [])), IfStmt(BinExpr(==, ArrayCell(arr, [Id(i), Id(j)]), IntegerLit(0)), BlockStmt([AssignStmt(Id(counter), BinExpr(+, Id(counter), IntegerLit(1)))]))]))])), IfStmt(BinExpr(>, Id(counter), BinExpr(-, IntegerLit(16), Id(counter))), BlockStmt([CallStmt(printString, StringLit(The entered matrix is a sparse matrix))]), CallStmt(printString, StringLit(The entered matrix is not a sparse matrix)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,362))
    def test_random_20(self):
        input = """main:function void(){
            n : integer;
            n = readInteger(); // a number between 100 and 999
            t : integer = n;
            a : integer;
            sum : integer = 0;
            while(t != 0){
                a = t%10;
                sum = a * a * a;
                t = t/10;
            } 
            if (sum == n) printString("This is Armstrong number!");
            else printString("This is not Armstrong number!");
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), VarDecl(t, IntegerType, Id(n)), VarDecl(a, IntegerType), VarDecl(sum, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(!=, Id(t), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(%, Id(t), IntegerLit(10))), AssignStmt(Id(sum), BinExpr(*, BinExpr(*, Id(a), Id(a)), Id(a))), AssignStmt(Id(t), BinExpr(/, Id(t), IntegerLit(10)))])), IfStmt(BinExpr(==, Id(sum), Id(n)), CallStmt(printString, StringLit(This is Armstrong number!)), CallStmt(printString, StringLit(This is not Armstrong number!)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,363))
    def test_random_21(self):
        input = """main:function void(){
            t : integer = n;
            a,i : integer;
            sum : integer = 0;
            for(i = 0, i < 500,i+1){
                while(t != 0){
                    a = t%10;
                    sum = a * a * a;
                    t = t/10;
                }
                if (sum == n) {printInteger(i); }
            }

        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(t, IntegerType, Id(n)), VarDecl(a, IntegerType), VarDecl(i, IntegerType), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(500)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(!=, Id(t), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(%, Id(t), IntegerLit(10))), AssignStmt(Id(sum), BinExpr(*, BinExpr(*, Id(a), Id(a)), Id(a))), AssignStmt(Id(t), BinExpr(/, Id(t), IntegerLit(10)))])), IfStmt(BinExpr(==, Id(sum), Id(n)), BlockStmt([CallStmt(printInteger, Id(i))]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,364))
    def test_random_22(self):
        input = """main: function void(){
            a : string = "Hello";
            b : string = "world";
            printString(a :: b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(Hello)), VarDecl(b, StringType, StringLit(world)), CallStmt(printString, BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,365))
    def test_random_23(self):
        input = """i: integer;
            func: function void() {
                for (i = 0, i < 10, i + 1) {
                    if (i % 2 == 0) {
                        continue;
                    }
                    writeInt(i);
                    if (i == 7) {
                        break;
                    }
                }
            }
        """
        expect = """Program([
	VarDecl(i, IntegerType)
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([ContinueStmt()])), CallStmt(writeInt, Id(i)), IfStmt(BinExpr(==, Id(i), IntegerLit(7)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,366))
    def test_random_24(self):
        input = """a: integer;
            func: function integer(x: integer) {
                a = x;
                while (a > 0) {
                    a = a - 1;
                    if (a == 5) {
                        return a;
                    }
                }
                return x;
            }"""
        expect = """Program([
	VarDecl(a, IntegerType)
	FuncDecl(func, IntegerType, [Param(x, IntegerType)], None, BlockStmt([AssignStmt(Id(a), Id(x)), WhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(5)), BlockStmt([ReturnStmt(Id(a))]))])), ReturnStmt(Id(x))]))
])"""
        self.assertTrue(TestAST.test(input,expect,367))
    def test_random_25(self):
        input = """func: function void() {
                    i = 1;
                    j = 1;
                    while (i < 10)
                        while (j < 10)
                            if (i < j) 
                                break;
                            writeInt(i + j);
                            j = j + 1;
                        i = i + 1;
                }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(i), IntegerLit(1)), AssignStmt(Id(j), IntegerLit(1)), WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), WhileStmt(BinExpr(<, Id(j), IntegerLit(10)), IfStmt(BinExpr(<, Id(i), Id(j)), BreakStmt()))), CallStmt(writeInt, BinExpr(+, Id(i), Id(j))), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,368))
    def test_random_26(self):
        input = """a: integer;
            func: function integer(x: integer) {
                a = x;
                do {
                    a = a - 1;
                    if (a == 5) {
                        return a;
                    }
                } while (a > 0);
                return x;
            }"""
        expect = """Program([
	VarDecl(a, IntegerType)
	FuncDecl(func, IntegerType, [Param(x, IntegerType)], None, BlockStmt([AssignStmt(Id(a), Id(x)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(5)), BlockStmt([ReturnStmt(Id(a))]))])), ReturnStmt(Id(x))]))
])"""
        self.assertTrue(TestAST.test(input,expect,369))
    def test_random_27(self):
        input = """func: function void() {
                    for( i = 1, i < 10, 1)
                        for (j = 1, j < 10, 1)
                            if (i < j)
                                break;
                            writeInt(i + j);
                }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), IntegerLit(1), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(10)), IntegerLit(1), IfStmt(BinExpr(<, Id(i), Id(j)), BreakStmt()))), CallStmt(writeInt, BinExpr(+, Id(i), Id(j)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,370))

    def test_cplx_1(self):
        input = """func: function void() {
                for (i = 1, i < 10, i + 1) {
                    if (i % 2 == 0) {
                        writeString("even");
                    } else {
                        writeString("odd");
                    }
                }
            }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(writeString, StringLit(even))]), BlockStmt([CallStmt(writeString, StringLit(odd))]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,371))
    def test_cplx_2(self):
        input = """main: function void() {
            exit: boolean;
            choice: string;
            writeString("Do you want to exit?");
            writeString("Enter Y/y for Yes, N/n for No.");
            choice = readString();
            if((choice == "y") || (choice == "Y")){
                exit = true;
            }   
            else exit = false;
            if(exit == true){
                printString("Goodbye!");
            }
            else printString("Please continue.");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(exit, BooleanType), VarDecl(choice, StringType), CallStmt(writeString, StringLit(Do you want to exit?)), CallStmt(writeString, StringLit(Enter Y/y for Yes, N/n for No.)), AssignStmt(Id(choice), FuncCall(readString, [])), IfStmt(BinExpr(||, BinExpr(==, Id(choice), StringLit(y)), BinExpr(==, Id(choice), StringLit(Y))), BlockStmt([AssignStmt(Id(exit), BooleanLit(True))]), AssignStmt(Id(exit), BooleanLit(True))), IfStmt(BinExpr(==, Id(exit), BooleanLit(True)), BlockStmt([CallStmt(printString, StringLit(Goodbye!))]), CallStmt(printString, StringLit(Please continue.)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,372))
    def test_cplx_3(self):
        input = """
        main: function void(){
            return 0;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input,expect,373))
    def test_cplx_4(self):
        input = """main: function void(){
            name: string;
            writeString("Enter your name");
            name = readString();
            greeting = "Hello!";
            printString(greeting :: name);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(name, StringType), CallStmt(writeString, StringLit(Enter your name)), AssignStmt(Id(name), FuncCall(readString, [])), AssignStmt(Id(greeting), StringLit(Hello!)), CallStmt(printString, BinExpr(::, Id(greeting), Id(name)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,374))
    def test_cplx_5(self):
        input = """a: array[5] of integer = {1, 2, 3, 4, 5};
                func: function integer(low: integer, high: integer) {
                    if ((low < 0) || (high < 0) || (low >= 5) || (high >= 5))
                        return -1;
                    sum = 0;
                    for (i = low, i <= high, i+1)
                        sum = sum + a[i];
                    return sum;
                }"""
        expect = """Program([
	VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(func, IntegerType, [Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(<, Id(low), IntegerLit(0)), BinExpr(<, Id(high), IntegerLit(0))), BinExpr(>=, Id(low), IntegerLit(5))), BinExpr(>=, Id(high), IntegerLit(5))), ReturnStmt(UnExpr(-, IntegerLit(1)))), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), Id(low)), BinExpr(<=, Id(i), Id(high)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(a, [Id(i)])))), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input,expect,375))
    def test_cplx_6(self):
        input = """func: function integer(n: integer) {
                    i = 1;
                    sum = 0;
                    while (i <= n) {
                        sum = sum + i;
                        i = i + 1;
                    }
                    return sum;
                }
                main: function void(){
                    n : integer;
                    n = readInteger();
                    printInteger(n * sum(n));
                }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(i), IntegerLit(1)), AssignStmt(Id(sum), IntegerLit(0)), WhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), CallStmt(printInteger, BinExpr(*, Id(n), FuncCall(sum, [Id(n)])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,376))
    def test_cplx_7(self):
        input = """func: function integer(n: integer) {
                    i = 1;
                    product = 1;
                    while (i <= n) {
                        product = product * i;
                        i = i + 1;
                    }
                    return product;
                }
                main: function void(){
                    n : integer;
                    n = readInteger();
                    printInteger(func(n));
                }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(i), IntegerLit(1)), AssignStmt(Id(product), IntegerLit(1)), WhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([AssignStmt(Id(product), BinExpr(*, Id(product), Id(i))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(product))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), CallStmt(printInteger, FuncCall(func, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,377))
    def test_cplx_8(self):
        input = """func: function integer(a: integer, b: integer) {
                    result = 1;
                    for (i = a, i <= b, i + 1) {
                        result = result * i;
                    }
                    return result;
                }
                main: function void(){
                    n,m : integer;
                    n = readInteger();
                    m = readInteger();
                    printInteger(func(n,m));
                }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([AssignStmt(Id(result), IntegerLit(1)), ForStmt(AssignStmt(Id(i), Id(a)), BinExpr(<=, Id(i), Id(b)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(*, Id(result), Id(i)))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(m, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), AssignStmt(Id(m), FuncCall(readInteger, [])), CallStmt(printInteger, FuncCall(func, [Id(n), Id(m)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,378))
    def test_cplx_9(self):
        input = """a: array[10] of integer;
                   i: integer;
        main: function void() {
            for (i = 0, i < 10, i + 1) {
                a[i] = i * i;
            }
            for (i = 0, i < 10, i + 1) {
                writeIntLn(a[i]);
            }
        }"""
        expect = """Program([
	VarDecl(a, ArrayType([10], IntegerType))
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(*, Id(i), Id(i)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeIntLn, ArrayCell(a, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,379))
    def test_cplx_10(self):
        input = """func: function void() {
                x : float;
                x = 1.0e-10;
                if (x != 0) {
                    x = 1 / x;
                }
            }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([VarDecl(x, FloatType), AssignStmt(Id(x), FloatLit(1e-10)), IfStmt(BinExpr(!=, Id(x), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(/, IntegerLit(1), Id(x)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,380))
    
    def test_cplxs_1(self):
        input = """func: function void() {
                do {
                    i = i + 1;
                    if (i % 2 == 0) {
                        continue;
                    }
                    if (i == 11) {
                        break;
                    }
                    writeInteger(i);
                } while (i < 20);
            }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(20)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([ContinueStmt()])), IfStmt(BinExpr(==, Id(i), IntegerLit(11)), BlockStmt([BreakStmt()])), CallStmt(writeInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,381))
    def test_cplxs_2(self):
        input = """i: integer;
            main: function void() {
                for (i = 0, i < 10, i + 1) {
                    if (i % 2 == 0) {
                        continue;
                    }
                    writeInt(i);
                    if (i == 7) {
                        break;
                    }
                }
            }"""
        expect = """Program([
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([ContinueStmt()])), CallStmt(writeInt, Id(i)), IfStmt(BinExpr(==, Id(i), IntegerLit(7)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,382))
    def test_cplxs_3(self):
        input = """
        findmax: function integer(arr: array [10] of integer){
            i : integer;
            max : integer = arr[0]; 
            for (i = 0, i < 10, i + 1) {
                if(max < arr[i]){
                    max = arr[i];
                }
            }
            return max;
        }
        main: function void(){
            arr: array [10] of integer;
            for (i = 0, i < 10, i + 1) {
                arr[i] = readInteger();
            }
            printInteger(findmax(arr));
        }"""
        expect = """Program([
	FuncDecl(findmax, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(max, IntegerType, ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(max), ArrayCell(arr, [Id(i)])), BlockStmt([AssignStmt(Id(max), ArrayCell(arr, [Id(i)]))]))])), ReturnStmt(Id(max))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i)]), FuncCall(readInteger, []))])), CallStmt(printInteger, FuncCall(findmax, [Id(arr)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,383))
    def test_cplxs_4(self):
        input = """
        // find min of 3 values
        findmin: function float(x: float, y:float,z:float,m:float){
            if(x < y){
                m = x;
            }
            else m = y;
            if(m < z) m  =z;
            return m;
        }
        main: function void(){
            x,y,z,m : float;
            x = readFloat();    
            y = readFloat();    
            z = readFloat();
            printString("MIN: ");
            printFloat(findmin(x,y,z,m));    
        }"""
        expect = """Program([
	FuncDecl(findmin, FloatType, [Param(x, FloatType), Param(y, FloatType), Param(z, FloatType), Param(m, FloatType)], None, BlockStmt([IfStmt(BinExpr(<, Id(x), Id(y)), BlockStmt([AssignStmt(Id(m), Id(x))]), AssignStmt(Id(m), Id(y))), IfStmt(BinExpr(<, Id(m), Id(z)), AssignStmt(Id(m), Id(z))), ReturnStmt(Id(m))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType), VarDecl(y, FloatType), VarDecl(z, FloatType), VarDecl(m, FloatType), AssignStmt(Id(x), FuncCall(readFloat, [])), AssignStmt(Id(y), FuncCall(readFloat, [])), AssignStmt(Id(z), FuncCall(readFloat, [])), CallStmt(printString, StringLit(MIN: )), CallStmt(printFloat, FuncCall(findmin, [Id(x), Id(y), Id(z), Id(m)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,384))
    def test_cplxs_5(self):
        input = """"""
        expect = """Program([
	
])"""
        self.assertTrue(TestAST.test(input,expect,385))
    def test_cplxs_6(self):
        input = """
        main: function void(){
            count : integer = 0;
            a : float;
            min: float;
            arr = readFloat();
            if(a > 0) {
                count = count +1 ;
            }
            min = a;
            while(a == 0){
                arr = readFloat(); 
                if (a < min) min = a;
                if(a > 0) {
                    count = count +1 ;
                }
            }
            printInteger(count);
            printFloat(min);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(count, IntegerType, IntegerLit(0)), VarDecl(a, FloatType), VarDecl(min, FloatType), AssignStmt(Id(arr), FuncCall(readFloat, [])), IfStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))])), AssignStmt(Id(min), Id(a)), WhileStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(arr), FuncCall(readFloat, [])), IfStmt(BinExpr(<, Id(a), Id(min)), AssignStmt(Id(min), Id(a))), IfStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), CallStmt(printInteger, Id(count)), CallStmt(printFloat, Id(min))]))
])"""
        self.assertTrue(TestAST.test(input,expect,386))
    def test_cplxs_7(self):
        input = """
        main: function void(){
            n : integer;
            sum: integer = 0;
            if(n < 0) {n = -n;}
            if ((n != 0) && (n % 10 == 0)){
                printInteger(-1);
                return 0;
            }
            while(n > sum)
            {
                sum = sum*10 + n % 10;
                n = n / 10;
            }
            if ( (n == sum) || (n == sum/10))  {
                printInteger(1);
            }
            else printInteger(-1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(sum, IntegerType, IntegerLit(0)), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(n), UnExpr(-, Id(n)))])), IfStmt(BinExpr(&&, BinExpr(!=, Id(n), IntegerLit(0)), BinExpr(==, BinExpr(%, Id(n), IntegerLit(10)), IntegerLit(0))), BlockStmt([CallStmt(printInteger, UnExpr(-, IntegerLit(1))), ReturnStmt(IntegerLit(0))])), WhileStmt(BinExpr(>, Id(n), Id(sum)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, BinExpr(*, Id(sum), IntegerLit(10)), BinExpr(%, Id(n), IntegerLit(10)))), AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(10)))])), IfStmt(BinExpr(||, BinExpr(==, Id(n), Id(sum)), BinExpr(==, Id(n), BinExpr(/, Id(sum), IntegerLit(10)))), BlockStmt([CallStmt(printInteger, IntegerLit(1))]), CallStmt(printInteger, UnExpr(-, IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,387))
    def test_cplxs_8(self):
        input = """
        isPrimeNumber: function boolean(n: integer){
            if(n < 2) return false;
            i :integer;
            for (i = 2, i <= n / 2, i+1) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }"""
        expect = """Program([
	FuncDecl(isPrimeNumber, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(BooleanLit(True))), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input,expect,388))
    def test_cplxs_9(self):
        input = """
        isPrimeNumber: function boolean(n: integer){
            if(n < 2) return false;
            i :integer;
            for (i = 2, i <= n / 2, i+1) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }
        main: function void(){
            n: integer;
            n = readInteger();
            if (isPrimeNumber(n) == true) {
                printString("n is prime number");
            } else{ printString("n is not prime number");  }
        }
        """
        expect = """Program([
	FuncDecl(isPrimeNumber, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(BooleanLit(True))), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, FuncCall(isPrimeNumber, [Id(n)]), BooleanLit(True)), BlockStmt([CallStmt(printString, StringLit(n is prime number))]), BlockStmt([CallStmt(printString, StringLit(n is not prime number))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,389))
    def test_cplxs_10(self):
        input = """
        isPrimeNumber: function boolean(n: integer){
            if(n < 2) return false;
            i :integer;
            for (i = 2, i <= n / 2, i+1) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }
        main: function void(){
            arr: array [10] of integer;
            if (n > 0) {
                m :integer = 1;
                i:integer = 0;
                do {            
                    if (isPrimeNumber(m) == 1) {                
                        arr[i] = m;
                        i= i + 1;
                    }
                    m = m+1;
                    
                } while( i!=n);
                printInteger(arr[i - 1]);
            }
            else printInteger(-1); 
        }"""
        expect = """Program([
	FuncDecl(isPrimeNumber, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(BooleanLit(True))), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), IfStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([VarDecl(m, IntegerType, IntegerLit(1)), VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(i), Id(n)), BlockStmt([IfStmt(BinExpr(==, FuncCall(isPrimeNumber, [Id(m)]), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i)]), Id(m)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(Id(m), BinExpr(+, Id(m), IntegerLit(1)))])), CallStmt(printInteger, ArrayCell(arr, [BinExpr(-, Id(i), IntegerLit(1))]))]), CallStmt(printInteger, UnExpr(-, IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,390))    
    
    def test_cplxs_11(self):
        input = """
        transposition: function void(arr : array [4,4] of integer;){
            for(j = 0, i < 4,i+1){
                for(i = 0, j < 4, j + 1){
                    printInteger(arr[i, j]);
                    printString(" ");
                }
            }
            printString("\\n");             
        }
        main: function void(){
            arr : array [4,4] of integer;
            i,j: integer;
            for(i = 0, i < 4,i+1){
                for(j = 0, j < 4, j + 1){
                    arr[i,j] = readInteger();
                }
            }    
        }"""
        expect = """Program([
	FuncDecl(transposition, VoidType, [Param(arr, ArrayType([4, 4], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(j)])), CallStmt(printString, StringLit( ))]))])), CallStmt(printString, StringLit(\\n))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([4, 4], IntegerType)), VarDecl(i, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), Id(j)]), FuncCall(readInteger, []))]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,391))
    def test_cplxs_12(self):
        input = """completeNum: function boolean(N : integer)
        {   
            sum : integer = 0;
            i : integer;
            for(i=1, i<=N/2 ,i+1){
                if(N%i==0) 
                    sum = sum + i;
            }
            if(sum==N){ return true;}
            else return false;
        }
        main: function void(){
            n : integer;
            n = readInteger();
            if(completedNum(n)){
                printString("n is complete number!");
            }
            else printString("n is not complete number!");
        }"""
        expect = """Program([
	FuncDecl(completeNum, BooleanType, [Param(N, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), BinExpr(/, Id(N), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(N), Id(i)), IntegerLit(0)), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))))])), IfStmt(BinExpr(==, Id(sum), Id(N)), BlockStmt([ReturnStmt(BooleanLit(True))]), ReturnStmt(BooleanLit(True)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(FuncCall(completedNum, [Id(n)]), BlockStmt([CallStmt(printString, StringLit(n is complete number!))]), CallStmt(printString, StringLit(n is not complete number!)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,392))
    def test_cplxs_13(self):
        input = """
        gcdIteration: function integer(p: integer, q: integer){
            if ((p == 0) || (q == 0)){
                return p + q;
            }
            while (q != p){
                if (p > q){
                    p = p - q; // a = a - b
                }else{
                    q = q- p;
                }
            }
            return p;
        }"""
        expect = """Program([
	FuncDecl(gcdIteration, IntegerType, [Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(p), IntegerLit(0)), BinExpr(==, Id(q), IntegerLit(0))), BlockStmt([ReturnStmt(BinExpr(+, Id(p), Id(q)))])), WhileStmt(BinExpr(!=, Id(q), Id(p)), BlockStmt([IfStmt(BinExpr(>, Id(p), Id(q)), BlockStmt([AssignStmt(Id(p), BinExpr(-, Id(p), Id(q)))]), BlockStmt([AssignStmt(Id(q), BinExpr(-, Id(q), Id(p)))]))])), ReturnStmt(Id(p))]))
])"""
        self.assertTrue(TestAST.test(input,expect,393))
    def test_cplxs_14(self):
        input = """
        gcdRecursion: function integer(p: integer, q: integer){
            if (q == 0) {
                return p;
            }
            else return gcdRecursion(q, p % q);
        }
        gcdIteration: function integer(p: integer, q: integer){
            if ((p == 0) || (q == 0)){
                return p + q;
            }
            while (q != p){
                if (p > q){
                    p = p - q; // a = a - b
                }else{
                    q = q- p;
                }
            }
            return p;
        }
        main: function void(){
            a,b: integer;
            do{
                a = readInteger();
            }while(a > 0);
            do{
                b = readInteger();
            }while(b > 0);
            printInteger(gcdRecursion(a,b));
            printString(" ")
            printInteger(gcdIteration(a,b));
        }
        """
        expect = """Program([
	FuncDecl(gcdRecursion, IntegerType, [Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(q), IntegerLit(0)), BlockStmt([ReturnStmt(Id(p))]), ReturnStmt(FuncCall(gcdRecursion, [Id(q), BinExpr(%, Id(p), Id(q))])))]))
	FuncDecl(gcdIteration, IntegerType, [Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(p), IntegerLit(0)), BinExpr(==, Id(q), IntegerLit(0))), BlockStmt([ReturnStmt(BinExpr(+, Id(p), Id(q)))])), WhileStmt(BinExpr(!=, Id(q), Id(p)), BlockStmt([IfStmt(BinExpr(>, Id(p), Id(q)), BlockStmt([AssignStmt(Id(p), BinExpr(-, Id(p), Id(q)))]), BlockStmt([AssignStmt(Id(q), BinExpr(-, Id(q), Id(p)))]))])), ReturnStmt(Id(p))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), FuncCall(readInteger, []))])), DoWhileStmt(BinExpr(>, Id(b), IntegerLit(0)), BlockStmt([AssignStmt(Id(b), FuncCall(readInteger, []))])), CallStmt(printInteger, FuncCall(gcdRecursion, [Id(a), Id(b)])), CallStmt(printString, StringLit( )), CallStmt(printInteger, FuncCall(gcdIteration, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,394))
    def test_cplxs_15(self):
        input = """
        swap:function void(out a: integer,out b: integer){
                tmp = a;
                a = b;
               b = tmp;
        }
        sapxep: function void (out arr : array [10] of integer){
            tmp : integer;
            for(i = 0, i < 4,i+1){
                for(j = i , j < 4,j+1){
                    if(arr[i] > arr[j]) swap(arr[j],arr[i]);
                }
            }
        }
        sortedSquares: function void(out arr : array [10] of integer){
            i : integer;
            for(i = 0, i < 9,i+1){
                arr[i] = arr[i] * arr[i];
            }
            sapxep(arr);
        }
        main: function void(){
            arr : array [10] of integer;
            for(i = 0, i < 10,i +1){
                arr[i] = readinteger();
            }
            sortedSquares(arr);
            for(i = 0, i < 10,i +1){
                printInteger(arr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(swap, VoidType, [OutParam(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([AssignStmt(Id(tmp), Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(tmp))]))
	FuncDecl(sapxep, VoidType, [OutParam(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(tmp, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), Id(i)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), CallStmt(swap, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [Id(i)])))]))]))]))
	FuncDecl(sortedSquares, VoidType, [OutParam(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(9)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i)]), BinExpr(*, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(i)])))])), CallStmt(sapxep, Id(arr))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i)]), FuncCall(readinteger, []))])), CallStmt(sortedSquares, Id(arr)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(arr, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,395))
    def test_cplxs_16(self):
        input = """
        fib: function integer(n : integer){
            if(n == 0) return 0;
            else if (n == 1) return 1;
            return fib(n - 1) + fib(n - 2);
        }
        infinite2DArray: function integer(x : integer, y: integer){
            if( (x == 0) && (y == 0)){return 0; }
            else if((x == 0) && (y == 1)){return 1;} else if( (x == 1) && (y == 0) ){return 1;}
            else if(x == 0){return fibonacci(y);} else if(y == 0){return fibonacci(x);}
            else{ return infinite2DArray(x - 1,y) + infinite2DArray(x ,y -1);}
        }
        main: function void(){
            a,b: integer;
            do{
                a = readInteger();
            }while(a > 0);
            do{
                b = readInteger();
            }while(b > 0);
            printInteger(infinite2DArray(a,b));
        }
        """
        expect = """Program([
	FuncDecl(fib, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(0)), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1)))), ReturnStmt(BinExpr(+, FuncCall(fib, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fib, [BinExpr(-, Id(n), IntegerLit(2))])))]))
	FuncDecl(infinite2DArray, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, Id(x), IntegerLit(0)), BinExpr(==, Id(y), IntegerLit(0))), BlockStmt([ReturnStmt(IntegerLit(0))]), IfStmt(BinExpr(&&, BinExpr(==, Id(x), IntegerLit(0)), BinExpr(==, Id(y), IntegerLit(1))), BlockStmt([ReturnStmt(IntegerLit(1))]), IfStmt(BinExpr(&&, BinExpr(==, Id(x), IntegerLit(1)), BinExpr(==, Id(y), IntegerLit(0))), BlockStmt([ReturnStmt(IntegerLit(1))]), IfStmt(BinExpr(==, Id(x), IntegerLit(0)), BlockStmt([ReturnStmt(FuncCall(fibonacci, [Id(y)]))]), IfStmt(BinExpr(==, Id(y), IntegerLit(0)), BlockStmt([ReturnStmt(FuncCall(fibonacci, [Id(x)]))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(infinite2DArray, [BinExpr(-, Id(x), IntegerLit(1)), Id(y)]), FuncCall(infinite2DArray, [Id(x), BinExpr(-, Id(y), IntegerLit(1))])))]))))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), FuncCall(readInteger, []))])), DoWhileStmt(BinExpr(>, Id(b), IntegerLit(0)), BlockStmt([AssignStmt(Id(b), FuncCall(readInteger, []))])), CallStmt(printInteger, FuncCall(infinite2DArray, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,396))
    def test_cplxs_17(self):
        input = """
        superPow: function integer(a : integer,b : integer){
            if (b == 0) {return 1;}
            else {
                luythua : integer;
                 luythua = superPow(a, b / 2);
                if ( (b % 2 )== 0) {return luythua * luythua; }
                else return (a * luythua * luythua) ;
            }
        }"""
        expect = """Program([
	FuncDecl(superPow, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(b), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([VarDecl(luythua, IntegerType), AssignStmt(Id(luythua), FuncCall(superPow, [Id(a), BinExpr(/, Id(b), IntegerLit(2))])), IfStmt(BinExpr(==, BinExpr(%, Id(b), IntegerLit(2)), IntegerLit(0)), BlockStmt([ReturnStmt(BinExpr(*, Id(luythua), Id(luythua)))]), ReturnStmt(BinExpr(*, BinExpr(*, Id(a), Id(luythua)), Id(luythua))))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,397))
    def test_cplxs_18(self):
        input = """
        search: function integer(out n : integer,m : integer,arr: array [5] of integer, index: integer){
            count,k,h :integer = 0,0,0;
            i: integer;
            for (i = 0, i < n, i+1){
                if( arr[i] == m){
                    count = i;
                    h = h + 1;
                    break;   
                }
            }
            if(h == 0) return -1;
            k = count;
            
            for(i = 0, i < n, i+1){
                if(i == count) {
                    arr[count] = arr[count + 1];
                        count = count + 1;
                    }
                }
                n = n - 1;
            return k;
        }"""
        expect = """Program([
	FuncDecl(search, IntegerType, [OutParam(n, IntegerType), Param(m, IntegerType), Param(arr, ArrayType([5], IntegerType)), Param(index, IntegerType)], None, BlockStmt([VarDecl(count, IntegerType, IntegerLit(0)), VarDecl(k, IntegerType, IntegerLit(0)), VarDecl(h, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(m)), BlockStmt([AssignStmt(Id(count), Id(i)), AssignStmt(Id(h), BinExpr(+, Id(h), IntegerLit(1))), BreakStmt()]))])), IfStmt(BinExpr(==, Id(h), IntegerLit(0)), ReturnStmt(UnExpr(-, IntegerLit(1)))), AssignStmt(Id(k), Id(count)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), Id(count)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(count)]), ArrayCell(arr, [BinExpr(+, Id(count), IntegerLit(1))])), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), ReturnStmt(Id(k))]))
])"""
        self.assertTrue(TestAST.test(input,expect,398))
    def test_cplxs_19(self):
        input = """
        calcPermutation : function integer(arr : array [5] of integer,n : integer){
            sum : integer = 0 ; 
            i : integer;
            for(i=0, i< 4, i+1){ 
                x : integer;
                x = abs(ar[i]- ar[i+1]);
                sum = sum + x ; 
            }
            return sum;

            }"""
        expect = """Program([
	FuncDecl(calcPermutation, IntegerType, [Param(arr, ArrayType([5], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), FuncCall(abs, [BinExpr(-, ArrayCell(ar, [Id(i)]), ArrayCell(ar, [BinExpr(+, Id(i), IntegerLit(1))]))])), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(x)))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input,expect,399))
    def test_cplxs_20(self):
        input = """        
        infinite2DArray: function integer(x : integer, y: integer){
            if( (x == 0) && (y == 0)){return 0; }
            else if((x == 0) && (y == 1)){return 1;} else if( (x == 1) && (y == 0) ){return 1;}
            else if(x == 0){return fibonacci(y);} else if(y == 0){return fibonacci(x);}
            else{ return infinite2DArray(x - 1,y) + infinite2DArray(x ,y -1);}
        }"""
        expect = """Program([
	FuncDecl(infinite2DArray, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, Id(x), IntegerLit(0)), BinExpr(==, Id(y), IntegerLit(0))), BlockStmt([ReturnStmt(IntegerLit(0))]), IfStmt(BinExpr(&&, BinExpr(==, Id(x), IntegerLit(0)), BinExpr(==, Id(y), IntegerLit(1))), BlockStmt([ReturnStmt(IntegerLit(1))]), IfStmt(BinExpr(&&, BinExpr(==, Id(x), IntegerLit(1)), BinExpr(==, Id(y), IntegerLit(0))), BlockStmt([ReturnStmt(IntegerLit(1))]), IfStmt(BinExpr(==, Id(x), IntegerLit(0)), BlockStmt([ReturnStmt(FuncCall(fibonacci, [Id(y)]))]), IfStmt(BinExpr(==, Id(y), IntegerLit(0)), BlockStmt([ReturnStmt(FuncCall(fibonacci, [Id(x)]))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(infinite2DArray, [BinExpr(-, Id(x), IntegerLit(1)), Id(y)]), FuncCall(infinite2DArray, [Id(x), BinExpr(-, Id(y), IntegerLit(1))])))]))))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,339))   