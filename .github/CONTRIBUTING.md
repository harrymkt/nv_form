# Contribution Guidelines
Thank you for the willingness to contribute!

## Guidelines
Before discussing about how you could contribute, please keep the following guidelines in mind to insure a safe environment, stability, and readability. Pull requests that do not follow the syntax or guidelines may be delayed or denied.

- Follow proper code syntax, see below.
- When creating pull requests it is advised that you create a new branch other than main and to commit on that branch only; this avoids issues during updating.
- We accept pull requests made with AI tools. However, you must insure that the implemented feature or change works correctly as expected, and that necessary tests are performed. Pull requests that do not follow this guideline will be rejected until such tests are performed. When you make a pull request that has code made with AI tools, you are responsible for performing the tests as you know the best of what prompts or how you did to construct the code.

### Code format
Use tab for indentation. Also, make sure operators are padded.

Good:
```
void test() {
	alert("hello", "testing");
}
```

Bad:
```
void test()
{
alert("hello","testing");
}
```

### Naming convention
- A class , method, function, namespace, and variable name must be snake lowercase, `my_class` is good, `myClass` and `MyClass` are not.
- The name of a constant variable, the one that never changes in runtime, must be snake uppercase, `MY_CONSTANT` is good, `MyConstant`, `my_constant`, and `myConstant` are not. This also applies to enum value names, but not the name of the enums itself. The name of the enum itself should be snake lowercase, i.e. just as the case of a namespace.
