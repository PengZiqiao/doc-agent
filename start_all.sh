#!/bin/bash

# 激活虚拟环境
source ./venv/bin/activate

echo "==================================="
echo "  启动 Doc Agent 项目"
echo "==================================="
echo ""

# 检查 .env 文件
if [ ! -f .env ]; then
    echo "错误：未找到 .env 文件"
    echo "请先创建 .env 文件并配置必要的环境变量"
    exit 1
fi

# 创建日志目录
mkdir -p logs

echo "[1/2] 启动后端服务 (LangGraph Dev)..."
langgraph dev > logs/backend.log 2>&1 &
BACKEND_PID=$!
echo "  后端服务已启动 (PID: $BACKEND_PID)"
echo "  日志: logs/backend.log"
echo ""

sleep 3

echo "[2/2] 启动前端服务 (Deep Agents UI)..."
cd deep-agents-ui
yarn dev > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..
echo "  前端服务已启动 (PID: $FRONTEND_PID)"
echo "  日志: logs/frontend.log"
echo ""

echo "==================================="
echo "  所有服务已启动！"
echo "==================================="
echo ""
echo "访问地址："
echo "  前端: http://localhost:3000"
echo "  后端: http://localhost:2024"
echo ""
echo "查看日志："
echo "  后端:   tail -f logs/backend.log"
echo "  前端:   tail -f logs/frontend.log"
echo ""
echo "停止所有服务："
echo "  kill $BACKEND_PID $FRONTEND_PID"
echo ""
echo "或使用停止脚本："
echo "  bash stop_all.sh"
echo ""
