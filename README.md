# serverless-tour
无服务架构在Python中应用场景实现。

使用JWT和AWS ApiGateway自定义授权程序的授权示例。

涉及到使用 4个 aws lambda function 授权到鉴权与刷新token 操作

jwt_sing_function(登录授权函数)

jwt_verify_function(授权校验函数)

jwt_gateway_function(统一分发函数)

jwt_refreshing_function(刷新授权函数)

整体构架：
    ![架构图!](jwt_function/image/architecture.png)

 

  