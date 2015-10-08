import sys
import os
import hashlib

def add_app_version(apk_file_name, client, service_id, env_id, env_name, to_version, json_version):
    custom_str = """{"url":"http://image.dlfx.qq.com/kl/android_publish2/app/apk_file_path", "size":"apk_size"}"""
    size = os.path.getsize(apk_file_name)
    hash = "1234"
    template = """{
        "full":
        {
            "url":"http://image.dlfx.qq.com/kl/android_publish/app/apk_file_path",
            "filesize":apk_size,
            "toversion":"to_version",
            "completedmd5":"file_hash", 
            "versionInterval":5,
            "fullapkname":"apk_file_path"
        }
    }"""
    template = template.replace("apk_file_path", apk_file_name)
    template = template.replace("apk_size", str(size))
    template = template.replace("to_version", to_version)
    template = template.replace("file_hash", hash)
    custom_str = custom_str.replace("apk_file_path", apk_file_name)
    custom_str = custom_str.replace("apk_size", str(size))
    json_file_name = "killer_android_" + json_version + ".json"
    f = open(json_file_name, "w")
    f.write(template)
    print(custom_str)
    print(template)

add_app_version("function.py", "hello", 1, 2, "test", "1.2.3.0", "1.2.3.4")
