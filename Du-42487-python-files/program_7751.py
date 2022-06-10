import subprocess

s = """
#include <stdio.h>

int fact(int n)
{{
    return (n) ? n * fact(n-1) : 1;
}}

int main()
{{
    printf("%d\\n", fact({:d}));
}}
"""

def factorial(n):
    with open("fact.c", "w") as f:
        f.write(s.format(n))
    with open("stdout.txt", "w+") as f:
        subprocess.run(["gcc", "fact.c", "-o", "out.o"])
        subprocess.run(["./out.o"], stdout=f)
        f.seek(0)
        return int(f.readline())
