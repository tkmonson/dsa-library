'''
Count Regex Strings

R is a valid regular expression if:
    1. R is 'a' or 'b'.
    2. R is of the form '(R_1 R_2)' where R_1 and R_2 are regular expressions.
    3. R is of the form '(R_1|R_2)' where R_1 and R_2 are regular expressions.
    4. R is of the form '(R_1*)' where R_1 is a regular expression.

Regular expressions can be nested and will always have two elements in the
parentheses. '*' will always be the second element; '(*a)' is invalid.

The set of strings recognized by R are as follows:
    1. If R is 'a' => 'a'.
    2. If R is 'b' => 'b'.
    3. If R is of the form '(R_1 R_2)' => all strings which can be obtained by
       a concatenation of strings s_1 and s_2, where s_1 is recognized by R_1
       and s_2 by R_2.
    4. If R is of the form '(R_1|R_2)' => the union of the sets of strings
       recognized by R_1 and R_2.
    5. If R is of the form '(R_1*)' => the concatenation of zero or more copies
       of any string recognized by R_1.

Given a regular expression R and an integer L, return the number of strings of
length L that are recognized by R.

-------------------------------------------------------------------------------

Solution is incomplete.
Look into NFA, DFA, Thompson's construction, and powerset/subset construction.
Regex => NFA => DFA => Minimize DFA => Matrix Exponentiation

'''

def count_strings(R: str, L: int):
    def helper(l_ptr, r_ptr):
        print(R[l_ptr : r_ptr + 1])
        if l_ptr == r_ptr:
            return

        l_ptr += 1
        r_ptr -= 1
        m_ptr = r_ptr
        if R[m_ptr] == ')':
            parens_val = 1
            while parens_val != 0:
                m_ptr -= 1
                if R[m_ptr] == '(':
                    parens_val -= 1
                if R[m_ptr] == ')':
                    parens_val += 1
        helper(m_ptr, r_ptr)
        m_ptr -= 1
        if R[m_ptr] == '|':
            m_ptr -= 1
        helper(l_ptr, m_ptr)

    helper(0, len(R) - 1)

if __name__ == '__main__':
    count_strings('((ab)((ab)|(ba)))', 0)

