// 10757 큰수 A+B
// [C]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void reverse(char arr[]) // 역순 정렬
{
    int len = strlen(arr);
    for (int i = 0; i < len / 2; i++)
    {
        char temp = arr[i];
        arr[i] = arr[len - i - 1];
        arr[len - i - 1] = temp;
    }
}
int main(void)
{
    char A[10002] = {0}, B[10002] = {0}, res[10003] = {0}; // 자리수를 뜻함
    int carry = 0, i;                                      //carry: 받아올림
    scanf("%s%s", A, B);
    reverse(A);
    reverse(B);

    int len = strlen(A) > strlen(B) ? strlen(A) : strlen(B);
    for (i = 0; i < len; i++)
    {
        int sum = A[i] - '0' + B[i] - '0' + carry;

        while (sum < 0)
            sum += '0';
        if (sum > 9)
            carry = 1;
        else
            carry = 0;
        res[i] = sum % 10 + '0'; //받아올림 후 남은 1의 자리 수의 아스키코드 저장
    }
    if (carry == 1)
        res[len] = '1'; //가장 큰 자릿수에서 받아올림이 발생하면 배열의 마지막에 1을 추가
    reverse(res);       //역순으로 정렬해 원하는 값으로 복원
    printf("%s", res);
    return 0;
}

// [python]
// a, b = map(int, input().split())
//print(a+b)
