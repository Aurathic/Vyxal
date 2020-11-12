codepage = "λ¬∧⟑∨⟇÷«»°\n․⍎½∆øÏÔÇæʀʁɾɽÞƈ∞⫙ß⎝⎠ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⎡⎣⨥⨪∺❝ð£¥§¦¡∂ÐřŠč√∖ẊȦȮḊĖẸṙ∑Ṡİ•\t"
codepage += "Ĥ⟨⟩ƛıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘŚśŜŝŞşšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƊƋƌƍƎ¢≈Ωªº"

commands = {
    '!': 'stack.push(len(stack))',
    '"': 'stack.shift(_RIGHT)',
    "'": 'stack.shift(_LEFT)',
    '$': 'stack.swap()',
    '%': 'rhs, lhs = stack.pop(2); stack.push(modulo(lhs, rhs))',
    '&': 'if VY_reg_reps % 2:VY_reg=stack.pop()\nelse:stack.push(VY_reg)\nVY_reg_reps += 1',
    '*': 'rhs, lhs = stack.pop(2); stack.push(multiply(lhs, rhs))',
    '+': 'rhs, lhs = stack.pop(2); stack.push(add(lhs, rhs))',
    ',': 'print(stack.pop(), end=""); printed = True',
    '-': 'rhs, lhs = stack.pop(2); stack.push(subtract(lhs, rhs))',
    '.': 'print(Vy_repr(stack.pop()), end=""); printed = True',
    '/': 'rhs, lhs = stack.pop(2); stack.push(divide(lhs, rhs))',
    ':': 'top = stack.pop(); stack.push(deref(top)); stack.push(deref(top))',
    '<': 'lhs, rhs = stack.pop(2); stack.push(int(rhs < lhs))',
    '=': 'lhs, rhs = stack.pop(2); stack.push(int(rhs == lhs))',
    '>': 'lhs, rhs = stack.pop(2); stack.push(int(rhs > lhs))',
    '?': 'stack.push(get_input())',
    'A': 'stack.push(stack.all())',
    'B': 'stack.push(Vy_int(stack.pop(), 2))',
    'C': 'stack.push(chrord(stack.pop()))',
    'D': 'top = stack.pop(); stack.push(top); stack.push(top); stack.push(top)',
    'E': 'x = stack.pop(); stack.push(eval(x))',
    'F': 'stack.do_filter(stack.pop())',
    'G': 'stack.push(max(stack.pop()))',
    'H': 'stack.push(Vy_int(stack.pop(), 16))',
    'I': 'stack.push(Vy_int(stack.pop()))',
    'J': 'rhs, lhs = stack.pop(2); stack.push(join(lhs, rhs))',
    'K': 'stack.push(divisors_of(stack.pop()))',
    'L': 'stack.push(len(stack.pop()))',
    'M': 'stack.do_map(stack.pop())',
    'N': 'top = stack.pop(); stack.push(to_number(top))',
    'O': 'lhs, rhs = stack.pop(2); stack.push(as_iter(rhs).count(lhs))',
    'P': 'y, x = stack.pop(2); stack.push(str(x).strip(str(y)))',
    'Q': 'exit()',
    'R': 'function, iterable = stack.pop(2); stack.push(Vy_reduce(function, as_iter(iterable)))',
    'S': 'stack.push(str(stack.pop()))',
    'T': 'stack.push([n for n in stack.pop() if bool(n)])',
    'U': 'stack.push(Vy_Uniquify(as_iter(stack.pop())))',
    'V': 'replacent, needle, haystack = stack.pop(3); stack.push(haystack.replace(needle, replacent))',
    'W': 'stack = Stack(Stack(stack.contents))',
    'X': 'if (_context_level) < _max_context_level: _context_level += 1',
    'Y': 'rhs, lhs = stack.pop(2); stack.push(interleave(as_iter(lhs), as_iter(rhs)))',
    'Z': 'lhs, rhs = stack.pop(2); stack.push(Stack(list(zip(rhs, lhs))))',
    '^': 'stack.reverse()',
    '_': 'stack.pop()',
    '`': 'stack.push("{}")',
    'a': 'stack.push(any(stack.pop()))',
    'b': 'stack.push(bin(stack.pop())[2:])',
    'c': 'lhs, rhs = stack.pop(2); stack.push(int(lhs in rhs))',
    'd': 'stack.push(stack.pop() * 2)',
    'e': 'lhs, rhs = stack.pop(2); stack.push(rhs ** lhs)',
    'f': 'stack.push(flatten(stack.pop())',
    'g': 'stack.push(min(stack.pop()))',
    'h': 'stack.push(stack.pop()[0])',
    'i': 'lhs, rhs = stack.pop(2); stack.push(as_iter(rhs)[lhs])',
    'j': 'lhs, rhs = stack.pop(2); stack.push(lhs.join([str(_item) for _item in as_iter(rhs)])); ',
    'l': 'stack.push([])',
    'm': 'p = stack.pop(); t = type(p); x = as_iter(p, str)[::-1]; stack.push(add(p, try_cast(x, t)))',
    'n': 'stack.push(_context_values[(_context_level - 1) % (len(_context_values) + 1)]);',
    'o': 'needle, haystack = stack.pop(2); stack.push(haystack.replace(needle, ""))',
    'p': 'y, x = stack.pop(2); stack.push(int(str(x).startswith(str(y)))',
    'q': 'stack.push('"' + str(stack.pop()) + '"')',
    'r': 'lhs, rhs = stack.pop(2); stack.push(orderless_range(rhs, lhs))',
    's': 'top = stack.pop(); stack.push(VySort(top))',
    't': 'stack.push(as_iter(stack.pop())[-1])',
    'u': 'stack.push(sort_unique(as_iter(stack.pop())))',
    'w': 'stack.push(Stack([stack.pop()]))',
    'x': '_context_level -= 1 * (1 - (_context_level == 1))',
    'y': 'x = uninterleave(stack.pop()); stack.push(x[0]), stack.push(x[1])',
    'z': 'stack.do_zipmap(stack.pop())',
    '~': 'stack.push(random.randint(-INT, INT))',
    '¬': 'stack.push(int(not stack.pop()))',
    '∧': 'lhs, rhs = stack.pop(2); stack.push(int(bool(rhs and lhs)))',
    '⟑': 'lhs, rhs = stack.pop(2); stack.push(rhs and lhs)',
    '∨': 'lhs, rhs = stack.pop(2); stack.push(int(bool(rhs or lhs)))',
    '⟇': 'lhs, rhs = stack.pop(2); stack.push(rhs or lhs)',
    '÷': 'for item in as_iter(stack.pop()): stack.push(item)',
    '⍎': 'fn = stack.pop(); stack += fn(stack)',
    'Ṛ': 'lhs, rhs = stack.pop(2); stack.push(random.randint(rhs, lhs))',
    'Ï': 'lhs, rhs = stack.pop(2); stack.push(as_iter(rhs).index(lhs))',
    'Ô': 'stack.push(Infinite_List(lambda x: (2 * (x - 1)) + 1))',
    'Ç': 'stack.push(subtract(1, stack.pop()))',
    'ʀ': 'stack.push(Stack(list(range(0, stack.pop() + 1))))',
    'ʁ': 'stack.push(Stack(list(range(0, stack.pop()))))',
    'ɾ': 'stack.push(Stack(list(range(1, stack.pop() + 1))))',
    'ɽ': 'stack.push(Stack(list(range(1, stack.pop()))))',
    'Þ': 'top = as_iter(stack.pop()); stack.push(top == top[::-1])',
    'ƈ': 'TODO',
    '∞': 'stack.push(Infinite_List(lambda x: x + 1))',
    'ß': 'TODO',
    "ř": "lhs, rhs = stack.pop(2); stack.push(repeat(rhs, lhs))",
    '∺': 'stack.push(stack.pop() % 2)',
    "œ": 'lhs, rhs = stack.pop(2); stack.push(vectorising_equals(modulo(rhs, lhs), 0))',
    '\n': '',
    '\t': '',
    "Ĥ": "stack.push(100)",
    "Ĵ": "stack.push(''.join(stack.pop())",
    "Ĳ": "stack.push('\\n'.join([str(x) for x in stack.pop()]))",
    "ĳ": "stack.push(10)",
    "ĵ": "x = stack.pop(); stack.push(multiply(x, x))",
    "∑": "stack.push(summate(stack.pop()))",
    "Ķ": "rhs, lhs = stack.pop(2); stack.push(Stack([lhs, rhs]))",
    "č": "stack.push(int(stack.pop() != 1))",
    "½": "stack.push(divide(stack.pop(), 2))",
    "⨪": "stack.push(subtract(stack.pop(), 1))",
    "⨥": "stack.push(add(stack.pop(), 1))",
    "ķ": "rhs, lhs = stack.pop(2); stack.push(list(orderless_range(lhs, rhs, 1)))",
    "ṙ": "stack.push(VyRound(stack.pop()))",
    "√": "stack.push(stack.pop() ** (1 / 2))",
    "∖": "rhs, lhs = stack.pop(2); stack.push(lhs // rhs)",
    "Ẋ": "rhs, lhs = stack.pop(2); stack.push(int((a or b) and not (a and b)))",
    "Ȧ": "stack.push(abs(stack.pop()))",
    "Ȯ": "stack.push(oct(stack.pop()))",
    "ĸ": "value, iterable = stack.pop(2); stack.push(distribute(iterable, value))",
    "Ĺ": "stack.push('\\n')",
    "ĺ": "stack.push(vertical_join(stack.pop()))",
    "Ļ": "padding, iterable = stack.pop(2); stack.push(vertical_join(iterable, padding))",
    "Ń": "n, fn = stack.pop(2); stack.do_fixed_gen(fn, n)",
    "ń": "stack.do_fixed_gen(stack.pop())",
    "Ň": "stack.push(math.factorial(stack.pop()))",
    "ņ": "stack.push(sums(as_iter(stack.pop())))",
    "Ň": "stack.push(int(len(set(as_iter(stack.pop()))) == 1))",
    "ð": "stack.push(' ')",
    "ň": "stack.push(counts(stack.pop()))",
    "ŉ": "p = stack.pop(); t = type(p); x = as_iter(p, str)[::-1]; stack.push(try_cast(x, t))",
    "Ŋ": "stack.push(Stack(as_iter(stack.pop(), str)[:-1]))",
    "⎝": "stack.push(min(stack.pop(), key=lambda x: x[-1]))",
    "ŋ": "x = summate(stack); stack = Stack(x)",
    "Ō": "stack.push(graded(as_iter(stack.pop())))",
    "ō": "stack.push(graded(as_iter(stack.pop()))[::-1])",
    "Ŏ": "stack.push(None)",
    "ŏ": "iterable, fn = stack.pop(2); stack.push(indexes_where(fn, iterable))",
    "Ő": "iterable, fn = stack.pop(2); stack.push(VySort(iterable, key=fn))",
    "ő": "VY_reg = stack.pop()",
    "⎠": "stack.push(max(stack.pop(), key=lambda x: x[-1]))",
    "Œ": "stack.push(multiply(stack.pop(), -1))",
    "Ŕ": "rhs, lhs = stack.pop(2); stack.push(vectorising_equals(lhs, rhs))",
    "ŕ": "rhs, lhs = stack.pop(2); stack.push(lhs != rhs)",
    "Ŗ": "stack.push(VY_reg)",
    "ŗ": "lhs, rhs = stack.pop(2); stack.push(as_iter(rhs)[lhs:])",
    "Ř": "rhs, lhs = stack.pop(2); stack.push(lshift(lhs, rhs))",
    "Ś": "rhs, lhs = stack.pop(2); stack.push(rshift(lhs, rhs))",
    "ś": "rhs, lhs = stack.pop(2); stack.push(bit_and(lhs, rhs))",
    "Ŝ": "rhs, lhs = stack.pop(2); stack.push(bit_or(lhs, rhs))",
    "ŝ": "rhs, lhs = stack.pop(2); stack.push(bit_xor(lhs, rhs))",
    "Ş": "stack.push(bit_not(stack.pop()))",
    "ş": "item, iterable = stack.pop(2); stack.push(prepend(as_iter(iterable), item))",
    "š": "item, index, iterable = stack.pop(3); stack.push(inserted(as_iter(iterable), index, item))",
    "Ţ": "stack.push(random_choice(as_iter(stack.pop())))",
    "ţ": "rhs, lhs = stack.pop(2); stack.push(int(lhs <= rhs))",
    "Ť": "rhs, lhs = stack.pop(2); stack.push(int(lhs >= rhs))",
    "ť": "if len(stack) >= 2: stack.push(stack[-2])\nelse: stack.push(get_input())"
    }
