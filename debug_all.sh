./debug.sh vkCmdDraw                     2>/dev/null | grep Counter
./debug.sh vkCmdDrawIndirect             2>/dev/null | grep Counter
./debug.sh vkCmdDrawIndirectCount        2>/dev/null | grep Counter
./debug.sh vkCmdDrawIndexed              2>/dev/null | grep Counter
./debug.sh vkCmdDrawIndexedIndirect      2>/dev/null | grep Counter
./debug.sh vkCmdDrawIndexedIndirectCount 2>/dev/null | grep Counter
./debug.sh vkCmdDrawIndexedRestart       2>/dev/null | grep Counter

