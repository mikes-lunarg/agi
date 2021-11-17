#!/bin/sh
set -e

bazel build -c dbg pkg
bazel build -c dbg //cmd/vulkan_sample

gapit trace -api vulkan -additionalargs -d=$1 -capture-frames 1 -out debug.gfxtrace ./bazel-bin/cmd/vulkan_sample/vulkan_sample
killall vulkan_sample

gapit commands debug.gfxtrace | grep vkCmdDraw
gapit profile debug.gfxtrace | grep GpuProfile | sed 's/{Counter/\n{Counter/g' | sed 's/{ID/\n{ID/g'


