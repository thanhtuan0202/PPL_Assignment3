import unittest
from TestUtils import TestChecker
from AST import *
from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC
class CheckerSuite(unittest.TestCase):
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """a : integer = 3;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_short_vardecl_1(self):
        """Test short variable declaration"""
        input = """a : integer = 3;
        main : function void(){
            b : float = 3;
            a = true;
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_short_vardecl_2(self):
        """Test short variable declaration"""
        input = """a : integer = 3;
        main : function void(){
            b : float = 3;
            a =b;
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_short_vardecl_3(self):
        """Test short variable declaration"""
        input = """a : integer = 3;
        foo: function auto(){}
        main : function void(){
            b : integer = foo();
            b = true + foo();
        }"""
        expect = "Type mismatch in expression: BinExpr(+, BooleanLit(True), FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_vardel(self):
        input = """a : integer = 3;
        foo: function auto(){}
        main : function void(){
            a = 4;
            b = a;
        }"""
        expect = "Undeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test_vardecl_1(self):
        input = """a : integer = 3;
        foo: function auto(){}
        main : function void(){
            a : boolean = true;
            b : integer = foo();
        }
        a:float  = 1.0;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test_vardecl_2(self):
        input = """a : integer = 3;
        foo: function auto(){}
        main : function void(){
            a : auto = true;
            b : integer = foo();
        }
        a:float  = 1.0;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 407))        
               
    def test_vardecl_3(self):
        input = """a : integer = 3;
        foo: function auto(){}
        main : function void(){
            a :auto;
        }
        a:float  = 1.0;"""
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_vardecl_4(self):
        input = """a : integer = 3;
        foo: function auto(){}
        main : function void(){
            a : array[3] of boolean = {true,true,false};
            b : integer = foo();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_vardecl_5(self):
        input = """a : integer = 3;
        foo: function auto(){}
        main : function void(){
            a : array[3] of auto = {true,true,false};
            b : integer = foo();
            c : boolean = a[1];
            c = a;
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(c), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_(self):
        input = """
        printInteger: function integer(){
            
        }
        main : function void(){
            a : array[3] of auto = {true,true,false};
            b : integer = foo();
            c : boolean = a[1];
            c = a;
        }"""
        expect = "Redeclared Function: printInteger"
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test_ifstmt(self):
        input = """
        main : function void(){
            a : array[3] of auto = {true,true,false};
            b : integer = 4;
            c : boolean = a[1];
            if(a[1]){
                printInteger(b);
            }
            else{
                printBoolean(c);
            }
            b : auto = 4;
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test_ifstmt(self):
        input = """
        main : function void(){
            a : array[3] of auto = {true,true,false};
            b : integer = 4;
            c : boolean = a[1];
            if(b){
                printInteger(b);
            }
            else{
                printBoolean(c);
            }
        }"""
        expect = "Type mismatch in statement: IfStmt(Id(b), BlockStmt([CallStmt(printInteger, Id(b))]), BlockStmt([CallStmt(printBoolean, Id(c))]))"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
        
    def test_ifstmt_2(self):
        input = """
        foo : function integer (a : auto, b : auto, c : auto){
            c = a + b;
           a = true;
        }
        main : function void(){
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test_auto_1(self):
        input = """
        foo : function float (a : auto){
            a = 3;
           return a;
        }
        main : function void(){
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))    

    def test_auto_2(self):
        input = """
        foo : function float (a : auto){
            b : auto = 3;
           return a;
        }
        main : function void(){
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))       
        
    def test_auto_3(self):
        input = """
        foo : function float (a : auto){
            b : auto = 3;
            c : integer = a + b;
            return true;
        }
        main : function void(){
        }"""
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 417)) 
        
    def test_auto_4(self):
        input = """
        foo : function float (a : array[3] of auto){
            b : auto = 3;
            a[1] = b;
            return a[0];
            a[0] = b + 3.0;
            return true;
        }
        main : function void(){
        }"""
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(+, Id(b), FloatLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 418)) 
        
    def test_auto_5(self):
        input = """
        foo : function auto (a : auto){
            b: auto = 3;
            a = 1.0;
            return b;
        }
        main : function void(){
            a : boolean = foo(1.0);
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, BooleanType, FuncCall(foo, [FloatLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 419)) 
        
    def test_auto_6(self):
        input = """
        foo : function auto (a : integer){
        }
        main : function void(){
            a : boolean = foo(3);
            b : integer = foo(4);
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, FuncCall(foo, [IntegerLit(4)]))"
        self.assertTrue(TestChecker.test(input, expect, 420)) 
    
    def test_auto_7(self):
        input = """
        foo : function auto (a : integer,b : array[3] of auto){
            b[0] = a;
        }
        main : function void(){
            foo(3,3);
        }"""
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3), IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 421)) 
        
    def test_auto_8(self):
        input = """
        foo : function auto (a : integer,b : array[3] of auto){
            b[0] = a;
        }
        main : function void(){
            foo(3,{1,2,3});
            a : integer = foo(3,{1,2,3});
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, [IntegerLit(3), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
        self.assertTrue(TestChecker.test(input, expect, 422)) 
        
    def test_auto_9(self):
        input = """
        foo : function auto (a : integer,b : array[3] of auto){
            b[0] = a;
        }
        main : function void(){
            foo(3,{1,2,3});
            a : integer = 3;
            b : auto = a;
            b: integer = 3;
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 423)) 

    def test_auto_10(self):
        input = """
        foo : function auto (a : integer,b : array[3] of auto){
            c : integer = a + b[0];
            printInteger(b[1]);
            b[2] = readInteger();
        }
        main : function void(){
            foo(3,{1,2,3});
            a : integer = foo(3,{1,2,3});
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, [IntegerLit(3), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
        self.assertTrue(TestChecker.test(input, expect, 424)) 
        
    def test_loop_1(self):
        input = """
        main: function void(){
            for( i = 0, i < 3, i +1){
                printInteger(i);
            }
        }
        """    
        expect = "Undeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect,425))
        
    def test_loop_2(self):
        input = """
        main: function void(){
            i : integer;
            for( i = 0, i + 3, i +1){
                printInteger(i);
            }
        }
        """    
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(+, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))"
        self.assertTrue(TestChecker.test(input, expect,426))       
    
    def test_loop_3(self):
        input = """
        main: function void(){
            i : float;
            for( i = 0, i < 3, i +1){
                printInteger(i);
            }
        }
        """    
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))"
        self.assertTrue(TestChecker.test(input, expect,427))
        
    def test_loop_4(self):
        input = """
        main: function void(){
            i : integer;
            a : boolean = true
            for( i = 0, i < 3, !a){
                printInteger(i);
            }
        }
        """    
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), UnExpr(!, Id(a)), BlockStmt([CallStmt(printInteger, Id(i))]))"
        self.assertTrue(TestChecker.test(input, expect,428))

    def test_loop_5(self):
        input = """
        main: function void(){
            i : auto;
            for( i = 0, i < 3, i +1){
                printInteger(i);
            }
            a : integer = i + 23;
        }
        """    
        expect = "Invalid Variable: i"
        self.assertTrue(TestChecker.test(input, expect,429))
        
    def test_loop_6(self):
        input = """
        main: function void(){
            i : integer;
            for( i = 0, i < 3, i +1){
                printInteger(i)
            }
        }
        """    
        expect = ""
        self.assertTrue(TestChecker.test(input, expect,430))
        
    def test_loop_7(self):
        input = """foo: function void(a : integer, out b : integer){
                while(a >= 1){
                    if( b % 2 == 1){ b = b * b;}
                    a = a + 1;
                }
                break;
            }
            main: function void(){
            }"""
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input,expect,431))    
    
    def test_loop_8(self):
        input = """foo: function void(a : integer, out b : integer){
                while(a >= 10){
                    if(b % 2 == 1) b = b * 2;
                    else b = b + 1;
                    a = a+ 1;
                }
                break;
            }
            main: function void(){
            }"""
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input,expect,432))   
        
    def test_loop_9(self):
        input = """foo: function void(a : integer, out b : integer){
                while(a >= 1){
                    if( b % 2 == 1){ b = b * b;}
                    a = a + 1;
                }
                break;
            }
            main: function void(){
            }"""
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input,expect,433))   
        
    def test_loop_10(self):
        input = """foo: function void(a : integer, out b : integer){
                while(a >= 1){
                    if( b % 2 == 1){ b = b * b;}
                    a = a + 1;
                }
                a = b + true;
            }
            main: function void(){
            }"""
        expect = """Type mismatch in expression: BinExpr(+, Id(b), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input,expect,434)) 
    
    def test_if_1(self):
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
        expect = "Undeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,435))
        
    def test_if_2(self):
        input = """foo: function void(a : integer,b :integer){
            i : integer;
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
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,436))
        
    def test_if_3(self):
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
        }
        main: function void(){}"""
        expect = "Undeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,437))
        
    def test_if_4(self):
        input = """foo: function void(a : integer,b :integer){
            if(a > 1){
                b = b *2;
            }else foo(a + 1,b);
        }
        main: function void(){
            foo(1,2.0)}"""
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,438))
        
    def test_if_5(self):
        input = """foo: function void(a : integer,b :integer){
            i  : integer;
            if(a > 1) for(i = 1,i < 4,i+1){
                if(a == 0){b = b + 1;}
                else b = b  + 4;
                b = b *2;
            }
            else {if(a == 0){
                b = b * b;
                continue;
            }
           }
        }
        main: function void(){}"""
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input,expect,439))
        
    def test_if_6(self):
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
        main: function void(){
            fib(true)}"""
        expect = "Type mismatch in statement: CallStmt(fib, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_if_auto(self):
        input = """
        foo: function boolean(a : integer,b : auto){
            if (b){
                return b;
            }
            else{
                return n;
            }
            super(1,2);
            return a;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Undeclared Variable: n"
        self.assertTrue(TestChecker.test(input,expect,456))    

    def test_if_auto_1(self):
        input = """
        test: function auto(a : integer){}
        foo: function boolean(a : integer,b : auto){
            if (b){
                return b;
            }
            else{
                return test(1);
            }
            return false;
        }
        main: function void(){
            a : string = test(3);
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(test, [IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input,expect,457)) 
        
    def test_if_auto_2(self):
        input = """
        test: function auto(a : integer){}
        foo: function boolean(a : integer,b : auto){
            if (test(1)){
                return b;
            }
            else{
                return test(1);
            }
            return false;
        }
        main: function void(){
            a : string = test(3);
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(test, [IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input,expect,458))   
        
    def test_if_auto_3(self):
        input = """
        test: function auto(a : integer){}
        foo: function boolean(a : integer,b : auto){
            if (b){
                return b;
            }
            else{
                return test(1);
            }
            return false;
        }
        main: function void(){
            a : string = test(3);
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(test, [IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input,expect,459)) 
        
    def test_if_auto_4(self):
        input = """
        test: function auto(a : integer){}
        foo: function boolean(a : integer,b : auto){
            a = 0;
            while( test(a)){
                a = a + 1;
            }
        }
        main: function void(){
            a : string = test(3);
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(test, [IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input,expect,460))              
    def test_inherit_1(self):
        input = """
        fib: function integer(n : integer,m:integer){
            
        }
        foo: function integer() inherit fib{
            super(1);
        }
        main: function void(){
            fib(true)}"""
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input,expect,441))       

    def test_inherit_2(self):
        input = """
        fib: function integer(n : integer,m:integer){
            
        }
        foo: function integer() inherit fib{
            preventDefault();
            a : integer = 3;
            a = true;
        }
        main: function void(){
            fib(true)}"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,442))   
        
    def test_inherit_3(self):
        input = """
        fib: function integer(inherit n : integer,m:integer){
            
        }
        foo: function integer() inherit fib{
            super(1);
            b : integer = n;
            
        }
        main: function void(){
            fib(true);}"""
        expect = "Type mismatch in statement: CallStmt(fib, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,443))   
        
    def test_inherit_4(self):
        input = """
         fib: function integer(inherit n : integer,m:integer){
            
        }
        foo: function integer() inherit fib{
            super();
            b : integer = n;
            
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input,expect,444))   
        
    def test_inherit_5(self):
        input = """
         fib: function integer(inherit n : integer,m:integer){
            
        }
        foo: function integer() inherit fib{
            super(1);
            b : integer = n;
            super(1);
        }
        main: function void(){
            fib(true);}
        """
        expect = "Invalid statement in function: super"
        self.assertTrue(TestChecker.test(input,expect,445))


    def test_inherit_6(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:integer){
            
        }
        foo: function integer(n : integer) inherit fib{
            super(n,2);
            b : integer = n;
            n = true;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Invalid Parameter: n"
        self.assertTrue(TestChecker.test(input,expect,446))
        
    def test_inherit_7(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:integer){
            
        }
        foo: function integer(a : integer) inherit fib{
            super(n,2);
            b : integer = n;
            n = true;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(n), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,447))
        
    def test_inherit_8(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:integer){
            
        }
        foo: function integer(a : integer) inherit fib{
            super(1,2);
            b : integer = n; 
            n = true;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(n), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,448))
        
    def test_inherit_9(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:integer){
            
        }
        foo: function integer(a : integer) inherit fib{
            super(1,2);
            b : integer = n; 
            if ( n > 1){
                return m;
            }
            else{
                return true;
            }
            return a;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,449))
        
    def test_inherit_10(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:integer){
            
        }
        foo: function integer(a : integer) inherit fib{
            super(1,2);
            b : integer = n; 
            if ( n > 1){
                return m;
            }
            else{
                return n;
            }
            return a;
            
            return 1.0;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in statement: CallStmt(fib, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,450))
        
    def test_inherit_11(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:float){
            
        }
        foo: function integer(a : integer) inherit fib{
            super(1,2);
            b : integer = n; 
            if ( n > 1){
                return m;
            }
            else{
                return n;
            }
            return a;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(m))"
        self.assertTrue(TestChecker.test(input,expect,451))
        
    def test_inherit_12(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:float){
            
        }
        foo: function integer(a : integer) inherit fib{
            b : integer = n; 
            if ( n > 1){
                return m;
            }
            else{
                return n;
            }
            return a;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input,expect,452))
        
    def test_inherit_13(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:float){
            
        }
        foo: function integer(a : integer) inherit fib{
            preventDefault()
            b : integer = n; 
            if ( n > 1){
                return m;
            }
            else{
                return n;
            }
            return a;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(m))"
        self.assertTrue(TestChecker.test(input,expect,453))
        
    def test_inherit_14(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:float){
            
        }
        foo: function integer(a : integer) inherit fib{
            super(1,2);
            b : integer = n; 
            if ( n > 1){
                return m;
            }
            else{
                return n;
            }
            super(1,2);
            return a;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(m))"
        self.assertTrue(TestChecker.test(input,expect,454))
        
    def test_inherit_15(self):
        input = """
         fib: function integer(inherit n : auto,inherit m:float){
            
        }
        foo: function integer(a : integer) inherit fib{
            super(1,2);
            b : integer = n; 
            if ( n > 1){
                return 10;
            }
            else{
                return n;
            }
            super(1,2);
            return a;
        }
        main: function void(){
            fib(true);}
        """
        expect = "Invalid statement in function: super"
        self.assertTrue(TestChecker.test(input,expect,455))
        
    def test_ramdon_1(self):
        input = """sum: function integer (out arr : array [4] of integer){
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
        }
        """
        expect = "Undeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,461))
        
    def test_ramdon_2(self):
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
        expect = "Undeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,462))
        
    def test_ramdon_3(self):
        input = """        main: function void(){
            n : integer;
            i: integer = 0;
            sum : float = 0.0;
            n = readInteger();
            while(i < n){
                sum = sum + 1 / i;
                i = i + 1;
            }
            writeFloats(sum);
        }
        """
        expect = "Undeclared Function: writeFloats"
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_ramdon_4(self):
        input = """sum: function integer (out arr : array [4] of integer){
            sum : integer = 0;
            i : integer = 0;
            for(i = 0, i < 2,i+1){
                sum = sum + arr[i];
            }
            return sum;
            sum : float = 0.0;
        }
        main: function void(){
            arr : array [4] of integer = {1,2,3,4};
            sum(arr);
            printInteger(arr[i]);
        }
        """
        expect = "Redeclared Variable: sum"
        self.assertTrue(TestChecker.test(input,expect,464))
        
    def test_ramdon_5(self):
        input = """sum: function integer (out arr : array [4] of integer){
            sum : integer = 0;
            i : integer = 0;
            for(i = 0, i < 2,i+1){
                arr : float = 0.0;
                sum = sum + arr[i];
                arr = arr + 1.0;
            }
            return sum;
            sum : float = 0.0;
        }
        main: function void(){
            arr : array [4] of integer = {1,2,3,4};
            sum(arr);
            printInteger(arr[i]);
        }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [Id(i)])"
        self.assertTrue(TestChecker.test(input,expect,465))
        
    def test_ramdon_6(self):
        input = """sum: function integer (out arr : array [4] of integer){
            sum : integer = 0;
            i : integer = 0;
            for(i = 0, i < 2,i+1){
                sum = sum + arr[i];
            }
            return sum;
        }
        main: function void(){
            arr : array [4] of integer = {1,2,3,4};
            sum : integer = 0;
            
            arr[1] = sum(arr);
            
            printInteger(arr[0]);
        }
        """
        expect = "Type mismatch in expression: FuncCall(sum, [Id(arr)])"
        self.assertTrue(TestChecker.test(input,expect,466))
 
    def test_ramdon_7(self):
        input = """a: array[5] of integer = {1, 2, 3, 4, 5};
                func: function integer(low: integer, high: integer) {
                    if ((low < 0) || (high < 0) || (low >= 5) || (high >= 5))
                        return -1;
    
                    sum = 0;
                    for (i = low, i <= high, i+1)
                        sum = sum + a[i];
                    return sum;
                }
        }
        """
        expect = "Undeclared Variable: sum"
        self.assertTrue(TestChecker.test(input,expect,467))   

    def test_ramdon_8(self):
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
        expect = "Undeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,468))    
        
    def test_ramdon_9(self):
        input = """ffunc: function void() {
            a : integer = 2;
            b : integer= 3;
            if (a > b) {
                writeString("a is greater than b");
            } else if (a < b) {
                writeString("a is less than b");
            } else {
                writeString("a is equal to b");
            }
        }
        """
        expect = "Undeclared Function: writeString"
        self.assertTrue(TestChecker.test(input,expect,469))   
        
    def test_ramdon_10(self):
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
        expect = "Undeclared Variable: max"
        self.assertTrue(TestChecker.test(input,expect,470))  
        
    def test_ramdon_11(self):
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
        }
        """
        expect = "Undeclared Function: writeString"
        self.assertTrue(TestChecker.test(input,expect,471)) 
        
         
    def test_ramdon_12(self):
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
        expect = "Undeclared Variable: max"
        self.assertTrue(TestChecker.test(input,expect,472))
        
    def test_ramdon_13(self):
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
        expect = "Undeclared Variable: max"
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_ramdon_14(self):
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
        expect = "Undeclared Variable: max"
        self.assertTrue(TestChecker.test(input,expect,474))
        
    def test_ramdon_15(self):
        input = """ain: function void(){
            name: string;
            writeString("Enter your name");
            name = readString();
            greeting = "Hello!";
            printString(greeting :: name);
        }
        """
        expect = "Undeclared Function: writeString"
        self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_cplx_1(self):
        input = """
        foo: function auto (a : integer, b : integer) inherit goo{
            
        }
        main: function void (){
            a = 3;
            foo(1,2);
            a : integer;
        }
        """
        expect = "Undeclared Function: goo"
        self.assertTrue(TestChecker.test(input,expect,476))          
        
    def test_cplx_2(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
            m : float = 3;
        }
        main: function void (){
            a = 3;
            foo(1,2);
            a : integer;
        }
        """
        expect = "Redeclared Variable: m"
        self.assertTrue(TestChecker.test(input,expect,477))     
        
    def test_cplx_3(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
        }
        main: function void (){
            a = 3;
            foo(1,2);
            a : integer;
        }
        """
        expect = "Undeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,478))      
        
    def test_cplx_4(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
            if( m > n){
                ret : integer = 1;
                
            }
            else{
                ret : integer = 0;
            }
            return ret;
        }
        main: function void (){
            a = 3;
            foo(1,2);
            a : integer;
        }
        """
        expect = "Undeclared Variable: ret"
        self.assertTrue(TestChecker.test(input,expect,479)) 
        
    def test_cplx_5(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
            ret : integer;
            if( m > n){
                ret = 1;
                
            }
            else{
                ret = 0;
            }
            return ret;
        }
        main: function void (){
            a : integer;
            a = 3;
            b : string = foo(1,2);
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, StringType, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input,expect,480))       
        
    def test_cplx_6(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
            ret : integer;
            if( m > n){
                ret = 1;
                
            }
            else{
                ret = 0;
            }
            return ret;
        }
        main: function void (){
            arr : array[3] of integer = {1,2.0,2};
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), FloatLit(2.0), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input,expect,481))      
        
    def test_cplx_7(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
            ret : integer;
            if( m > n){
                ret = 1;
                
            }
            else{
                ret = 0;
            }
            return ret;
        }
        main: function void (){
            arr : array[3] of integer = {1,2,2};
            arr = foo(1,2);
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(arr), FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_cplx_8(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
            ret : integer;
            if( m > n){
                ret = 1;
                
            }
            else{
                ret = 0;
            }
            return ret;
        }
        main: function void (){
            arr : array[3] of float = {1,2.0,2};
            arr = foo(1,2);
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(arr), FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input,expect,483))            
        
    def test_cplx_9(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
            ret : integer;
            if( m > n){
                ret = 1;
                
            }
            else{
                ret = 0;
            }
            return ret;
        }
        main: function void (){
            arr : array[3] of integer = {1,2.0,2};
            arr = foo(1,2);
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), FloatLit(2.0), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input,expect,484)) 
        
    def test_cplx_10(self):
        input = """
        glo : integer = 3;
        goo : function integer(inherit m : integer, inherit n: integer){
            
        }
        foo: function auto (a : integer, b : integer) inherit goo{
            super(m,n);
            ret : integer;
            if( m > n){
                ret = 1;
                
            }
            else{
                ret = 0;
            }
            return ret;
        }
        main: function void (){
            arr : array[3] of auto = {1,2.0,2};
            a : auto = arr[1];
            b : boolean = a + arr[1];
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, BooleanType, BinExpr(+, Id(a), ArrayCell(arr, [IntegerLit(1)])))"
        self.assertTrue(TestChecker.test(input,expect,485)) 
        
    def test_cplx_11(self):
        input = """
        printInteger: function void(){
            
        }
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
        expect = "Redeclared Function: printInteger"
        self.assertTrue(TestChecker.test(input,expect,486))
        
    def test_cplx_12(self):
        input = """
        a :integer = 3;
        a : float = 4;
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
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_cplx_13(self):
        input = """
        main: function void(){
            n = 3;
        }
        n :integer;"""
        expect = "Undeclared Variable: n"
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_cplx_14(self):
        input = """swap:function void(out a: integer,out b: integer){
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
        }"""
        expect = "Undeclared Variable: tmp"
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test_cplx_15(self):
        input = """swap:function void(out a: integer,out b: integer){
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
        }"""
        expect = "Undeclared Variable: tmp"
        self.assertTrue(TestChecker.test(input,expect,490))
        
    def test_cplx_16(self):
        input = """
        n : integer;
        main: function void(){
            n : float;
            {
                n : boolean;
                n = 2;
            }
            n = 1;
            n = 2.0;
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(n), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,491))
        
    def test_cplx_17(self):
        input = """
        foo: function void(a : auto){
            if(!a){
                a = 2;
            }
        }
        main: function void(){
            n : float;
            {
                n : boolean;
            }
            n = 1;
            n = 2.0;
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,492))
        
    def test_cplx_18(self):
        input = """
        foo: function void(a : auto,b:auto){
            c : integer = 3 + b;
            b = 3.0;
        }
        main: function void(){
            n : float;
            {
                n : boolean;
            }
            n = 1;
            n = 2.0;
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(b), FloatLit(3.0))"
        self.assertTrue(TestChecker.test(input,expect,493))
        
    def test_cplx_19(self):
        input = """
        foo: function void(a : auto,b:auto,a : float){
            c : integer = 3 + b;
            b = 3.0;
        }
        main: function void(){
            n : float;
            {
                n : boolean;
            }
            n = 1;
            n = 2.0;
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,494))
        
    def test_cplx_20(self):
        input = """
        c : integer;
        foo: function void(a : auto,b:auto){
            c : integer = 3 + b;
        }
        main: function void(){
            n : float;
            {
                n : boolean;
            }
            n = 1;
            n = 2.0;
        }
        c : float;"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,495))
        
    def test_cplx_21(self):
        input = """x,y: array[2] of integer;
        a,b: array[2] of boolean;
        printInteger: integer ;
        //main: function void(){}
"""
        expect = "Redeclared Variable: printInteger"
        self.assertTrue(TestChecker.test(input,expect,496))
        
    def test_cplx_22(self):
        input = """
        goo :  function void(a : integer){}
        foo: function void  () inherit goo{
            a : integer = true;
        }
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,497))
        
    def test_cplx_23(self):
        input = """
        goo :  function void(inherit a : integer){}
        foo: function void  () inherit goo{
            super(a);
            a : integer = true;
        }
        main: function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,498))
        
    def test_cplx_24(self):
        input = """
        goo :  function void(inherit a : integer){}
        foo: function void  () inherit goo{
            super(a);
            a : integer = true;
        }
        main: function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,499))
        
    def test_cplx_25(self):
        input = """
        goo :  function void(inherit a : integer){}
        foo: function void  () inherit goo{
            super(a);
            a : integer = true;
        }
        main: function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,500))