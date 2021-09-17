
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftIMPLICATIONleftANDleftNEGATIVEAND COMMA CONST DIMPLICATION IMPLICATION LETTERS LPAREN NEGATIVE OR RPARENexpr : LETTERSexpr : NEGATIVE exprexpr : LPAREN expr RPARENexpr : expr AND exprexpr : expr OR exprexpr : expr IMPLICATION exprexpr : expr DIMPLICATION exprexpr : expr COMMA exprexpr : COMMAexpr : CONST'
    
_lr_action_items = {'LETTERS':([0,3,4,7,8,9,10,11,],[2,2,2,2,2,2,2,2,]),'NEGATIVE':([0,3,4,7,8,9,10,11,],[3,3,3,3,3,3,3,3,]),'LPAREN':([0,3,4,7,8,9,10,11,],[4,4,4,4,4,4,4,4,]),'COMMA':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[5,11,-1,5,5,-9,-10,5,5,5,5,5,-2,11,-4,-5,-6,11,11,-3,]),'CONST':([0,3,4,7,8,9,10,11,],[6,6,6,6,6,6,6,6,]),'$end':([1,2,5,6,12,14,15,16,17,18,19,],[0,-1,-9,-10,-2,-4,-5,-6,-7,-8,-3,]),'AND':([1,2,5,6,12,13,14,15,16,17,18,19,],[7,-1,-9,-10,-2,7,-4,7,7,7,7,-3,]),'OR':([1,2,5,6,12,13,14,15,16,17,18,19,],[8,-1,-9,-10,-2,8,-4,-5,-6,8,8,-3,]),'IMPLICATION':([1,2,5,6,12,13,14,15,16,17,18,19,],[9,-1,-9,-10,-2,9,-4,9,-6,9,9,-3,]),'DIMPLICATION':([1,2,5,6,12,13,14,15,16,17,18,19,],[10,-1,-9,-10,-2,10,-4,-5,-6,10,10,-3,]),'RPAREN':([2,5,6,12,13,14,15,16,17,18,19,],[-1,-9,-10,-2,19,-4,-5,-6,-7,-8,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,3,4,7,8,9,10,11,],[1,12,13,14,15,16,17,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> LETTERS','expr',1,'p_neg3','lexer.py',50),
  ('expr -> NEGATIVE expr','expr',2,'p_neg2','lexer.py',55),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_par','lexer.py',60),
  ('expr -> expr AND expr','expr',3,'p_andexp','lexer.py',65),
  ('expr -> expr OR expr','expr',3,'p_orexp','lexer.py',72),
  ('expr -> expr IMPLICATION expr','expr',3,'p_impli','lexer.py',80),
  ('expr -> expr DIMPLICATION expr','expr',3,'p_dimpli','lexer.py',86),
  ('expr -> expr COMMA expr','expr',3,'p_comma','lexer.py',92),
  ('expr -> COMMA','expr',1,'p_comma1','lexer.py',98),
  ('expr -> CONST','expr',1,'p_const','lexer.py',103),
]
