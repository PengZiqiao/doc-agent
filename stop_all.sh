#!/bin/bash

echo "==================================="
echo "  停止 Doc Agent 项目"
echo "==================================="
echo ""

# 查找并停止后端服务
BACKEND_PID=$(pgrep -f "langgraph dev")
if [ -n "$BACKEND_PID" ]; then
    echo "停止后端服务 (PID: $BACKEND_PID)..."
    kill $BACKEND_PID
    echo "  ✓ 后端服务已停止"
else
    echo "  - 后端服务未运行"
fi

# 查找并停止前端服务
FRONTEND_PID=$(pgrep -f "yarn dev")
if [ -n "$FRONTEND_PID" ]; then
    echo "停止前端服务 (PID: $FRONTEND_PID)..."
    kill $FRONTEND_PID
    echo "  ✓ 前端服务已停止"
else
    echo "  - 前端服务未运行"
fi

echo ""
echo "==================================="
echo "  所有服务已停止"
echo "==================================="
