'''
Accounts Merge (#721)

Given a list `accounts` where each element `accounts[i]` is a list of strings,
each element `accounts[i][0]` is a name, and the rest of the elements in
`accounts[i]` are email addresses of the account, merge any accounts that share
an email address and return the list of accounts such that each name is
followed by all of the email addresses associated with the account in sorted
order.

Two accounts can have the same name but belong to different people (because
two different people could have the same name). If two accounts share an email
address, they belong to the same person (thus, any accounts that have the same
email address necessarily have the same name).
'''

from collections import defaultdict

exec(open('_parent_import.py').read())
from structures.disjoint_set import DisjointSet

def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    uf = DisjointSet(len(accounts))

    # Creat unions between indexes
    ownership = {}
    for i, (_, *emails) in enumerate(accounts):
        for email in emails:
            if email in ownership:
                uf.union(i, ownership[email])
            ownership[email] = i

    # Append emails to correct index
    ans = defaultdict(list)
    for email, owner in ownership.items():
        ans[uf.find(owner)].append(email)

    return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

'''
As this problem involves merging (or unioning) accounts, the disjoint-set data
structure is a natural choice. The elements of the disjoint sets are the
indicies of the accounts. Each email address in the input is read and if one
has been read previously, its account is unioned with the account where it was
read previously. Every distinct email address is now associated with the
account where it was last read. This is where the disjoint-set data structure
has a great advantage: find (O(logn) first call, O(1) subsequent call) is
called on each of these accounts to find the unioned account that each email
will be added to.
'''

def accounts_merge2(accounts: list[list[str]]) -> list[list[str]]:
    n = len(accounts)
    email_sets = [set(account[1:]) for account in accounts]
    i = 0
    while i < n:
        if not email_sets[i]:
            i += 1
            continue
        merge_occurred = False
        j = i + 1
        while j < n:
            if email_sets[i].intersection(email_sets[j]):
                email_sets[i] = email_sets[i].union(email_sets[j])
                email_sets[j] = {}
                merge_occurred = True
            j += 1
        if not merge_occurred:
            i += 1

    result = []
    for i in range(n):
        if email_sets[i]:
            result.append([accounts[i][0]] + sorted(list(email_sets[i])))

    return result

'''
This is my initial solution that does not use a disjoint-set data structure.
It passes all test cases but is slow. Given a = [['John', 'email1', 'email2'],
['John', 'email3', 'email4'], ['John', 'email2', 'email3']], if you compare the
set of emails in a[0] to those in the other accounts in a linear fashion, you
will know that a[2] should be unioned with a[0], but you won't know that a[1]
should, too. You would have to union a[0] and a[2] and then consider a[1] with
regard to that union. I thought of this concept in terms of distance: a[2] is a
distance of 1 from a[0], a[1] is a distance of 2 from a[0]. So, in order to
find all of the email addresses to be unioned under account a[0], you could
union a[0] with all of the 1-distance accounts, then loop through all of the
accounts again to consider all remaining 2-distance accounts, then again with
the remaining 3-distance accounts, and so on, until a merge does not occur
during a loop.
'''

if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    print(accounts_merge(accounts))

