syntax =  {'formats': {'builtin': '%(syntax_builtin)s',
             'comment': '%(syntax_comment)s',
             'hexnumber': '%(syntax_number)s',
             'keyword': '%(syntax_keyword)s',
             'number': '%(syntax_number)s',
             'proper_object': '%(syntax_proper_object)s',
             'operators': '%(syntax_operators)s',
             'braces': '%(syntax_braces)s',
             'definition': '%(syntax_definition)s',
             'highlight_word': '%(syntax_highlight_word)s',
             'string': '%(syntax_string)s'},
 'partitions': [('comment', '#', '\n'),
                ('string', "[bruBRU]?'''", "'''", True),
                ('string', "[bruBRU]?'", "'"),
                ('string', '[bruBRU]?"""', '"""', True),
                ('string', '[bruBRU]?"', '"')],
 'scanner': {None: [('hexnumber', '(0x)([0-9a-fA-F])+?'),
                    ('number', '\\d+(\\.\\d*)?'),
                    #('definition',
                        #'\\s*\\bdef\\b\\s*(\\w+)|\\s*\\bclass\\b\\s*(\\w+)'),
                    ('proper_object', ['self']),
                    #('highlight_word', 'error'),
                    ('braces', ['\\(', '\\)', '\\[', '\\]']),
                    ('operators',
                     ['\\+',
                      '\\=',
                     ]),
                    ('keyword',
                     ['and',
                      'as',
                      'assert',
                      'break',
                      'class',
                      'continue',
                      'def',
                      'del',
                      'elif',
                      'else',
                      'except',
                      'exec',
                      'finally',
                      'for',
                      'from',
                      'global',
                      'if',
                      'import',
                      'in',
                      'is',
                      'lambda',
                      'not',
                      'or',
                      'pass',
                      'print',
                      'raise',
                      'return',
                      'try',
                      'while',
                      'with',
                      'yield'],
                     '(^|[\x08\\W])',
                     '[\\x08\\W]'),
                    ('builtin',
                     ['ArithmeticError',
                      'AssertionError',
                      'AttributeError',
                      'BaseException',
                      'BufferError',
                      'BytesWarning',
                      'DeprecationWarning',
                      'EOFError',
                      'Ellipsis',
                      'EnvironmentError',
                      'Exception',
                      'False',
                      'FloatingPointError',
                      'FutureWarning',
                      'GeneratorExit',
                      'IOError',
                      'ImportError',
                      'ImportWarning',
                      'IndentationError',
                      'IndexError',
                      'KeyError',
                      'KeyboardInterrupt',
                      'LookupError',
                      'MemoryError',
                      'NameError',
                      'None',
                      'NotImplemented',
                      'NotImplementedError',
                      'OSError',
                      'OverflowError',
                      'PendingDeprecationWarning',
                      'ReferenceError',
                      'RuntimeError',
                      'RuntimeWarning',
                      'StandardError',
                      'StopIteration',
                      'SyntaxError',
                      'SyntaxWarning',
                      'SystemError',
                      'SystemExit',
                      'TabError',
                      'True',
                      'TypeError',
                      'UnboundLocalError',
                      'UnicodeDecodeError',
                      'UnicodeEncodeError',
                      'UnicodeError',
                      'UnicodeTranslateError',
                      'UnicodeWarning',
                      'UserWarning',
                      'ValueError',
                      'Warning',
                      'ZeroDivisionError',
                      '__import__',
                      'abs',
                      'all',
                      'any',
                      'apply',
                      'basestring',
                      'bin',
                      'bool',
                      'buffer',
                      'bytearray',
                      'bytes',
                      'callable',
                      'chr',
                      'classmethod',
                      'cmp',
                      'coerce',
                      'compile',
                      'complex',
                      'copyright',
                      'credits',
                      'delattr',
                      'dict',
                      'dir',
                      'divmod',
                      'enumerate',
                      'eval',
                      'execfile',
                      'exit',
                      'file',
                      'filter',
                      'float',
                      'format',
                      'frozenset',
                      'getattr',
                      'globals',
                      'hasattr',
                      'hash',
                      'help',
                      'hex',
                      'id',
                      'input',
                      'int',
                      'intern',
                      'isinstance',
                      'issubclass',
                      'iter',
                      'len',
                      'license',
                      'list',
                      'locals',
                      'long',
                      'map',
                      'max',
                      'memoryview',
                      'min',
                      'next',
                      'object',
                      'oct',
                      'open',
                      'ord',
                      'pow',
                      'print',
                      'property',
                      'quit',
                      'range',
                      'raw_input',
                      'reduce',
                      'reload',
                      'repr',
                      'reversed',
                      'round',
                      'set',
                      'setattr',
                      'slice',
                      'sorted',
                      'staticmethod',
                      'str',
                      'sum',
                      'super',
                      'tuple',
                      'type',
                      'unichr',
                      'unicode',
                      'vars',
                      'xrange',
                      'zip'],
                     '(^|[^\\.\\w])??(?<!\w)',
                     '[\\x08\\W]??'),
                    ('ident', '[A-Za-z_][A-Za-z_0-9]*?')]}}
