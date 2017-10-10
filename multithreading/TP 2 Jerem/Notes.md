## Warmup

### Naive

For this example, the expected result should be 1. Or, in my case, the
result is 4. So we can assume that multiple threads are trying to access
the counter at the same time, and some operations cannot be done

## First improvement

Toto

## Spooler

### Naive

For this version, we notice that every thread is going to print its pages one
by one and it is not the default behavior of a printer. One document should be
print entirely before trying to print the others.