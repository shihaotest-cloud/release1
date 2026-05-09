from translate import Translator

def en_to_zh(text):
    # 翻译：英文 -> 中文
    translator = Translator(from_lang="english", to_lang="chinese")
    result = translator.translate(text)
    return result

if __name__ == "__main__":
    print("===== 英文翻译中文小工具 =====")
    while True:
        # 输入英文
        en_text = input("\n请输入要翻译的英文(输入quit退出)：")
        if en_text.lower() == "quit":
            print("程序退出")
            break
        # 翻译并输出
        zh_text = en_to_zh(en_text)
        print("翻译结果：", zh_text)