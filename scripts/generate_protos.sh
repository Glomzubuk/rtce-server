# Usage: scripts/generate_protos.cmd
#
# Generate the python protobuf implementation

python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/session.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbadmin/account.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbadmin/audit.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbadmin/config.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbadmin/match.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbadmin/report.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbadmin/shop.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbadmin/stats.proto
touch tbadmin/__init__.py
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/account.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/crash.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/event.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/lobby.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/log.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/match.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/query.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/session.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/shop.proto
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbmatch/user.proto
touch tbmatch/__init__.py
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbrpc/tbrpc.proto
touch tbrpc/__init__.py
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbui/tbcharacter.proto
touch tbui/__init__.py
python -m grpc_tools.protoc -Iprotos --python_out=. protos/tbportal/portal.proto
touch tbportal/__init__.py
