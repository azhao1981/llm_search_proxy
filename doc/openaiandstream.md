

https://platform.openai.com/docs/api-reference/chat

https://platform.openai.com/docs/api-reference/streaming

```bash
# -S 流式
xh -S post http://localhost:8068/openai/v1/chat/completions name=weiz

curl -N -X POST http://localhost:8068/openai/v1/chat/completions -H "Content-Type: application/json" -d '{"name":"weiz"}'

echo '{"name":"weiz"}' | websocat -n1 -b ws://localhost:8068/openai/v1/chat/completions

http --stream POST http://localhost:8068/openai/v1/chat/completions name=weiz
```
