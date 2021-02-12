# 금액의 최솟값

A, B, C, X, Y = map(int,input().split()) # 양념, 후라이드, 반반

# x, y = 양념 x마리, 후라이드 y마리
if A + B < 2 * C :
    print(A * X + B * Y)
else :
    ans = 2 * C * min(X,Y)
    if X >= Y :
        value = X - Y
        ans += min(A*value , 2 * C* value)
    else :
        value = Y - X
        ans += min(B*value , 2 * C * value)

    print(ans)