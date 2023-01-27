load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library")


######################
## Switch-ML builds ##
######################

cc_binary(
    name = "main",
    srcs = ["src/main.cpp"],
    deps = [
        "@arrayfire//:arrayfire",
        "@oneDNN//:oneDNN",
        "@flashlight//:flashlight",
    ],
    linkstatic=True,
    visibility = ["//visibility:public"],
)

