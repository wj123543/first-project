from pathlib import Path
import json
from collections import Counter

# 函数1：读取文本文件，过滤空行
def load_lines(path: str | Path) -> list[str]:
    p = Path(path)
    lines = []
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                lines.append(clean_line)
    return lines

# 函数测试
if __name__ == "__main__":
    test_load = load_lines("data/week02_sentences.txt")
    print("【load_lines测试】读取句子总数：", len(test_load))

# 函数2：文本标准化清洗
def normalize_text(text: str) -> str:
    text = text.lower()
    text = " ".join(text.split())
    return text

# 函数测试
test_norm = normalize_text("  Hello   NLP！")
print("【normalize_text测试】清洗结果：", test_norm)

# 函数3：统计全部词频
def count_tokens(lines: list[str]) -> Counter:
    all_words = []
    for sent in lines:
        clean_sent = normalize_text(sent)
        words = clean_sent.split()
        all_words.extend(words)
    return Counter(all_words)

# 函数测试
test_count = count_tokens(["python easy", "python nlp"])
print("【count_tokens测试】词频：", test_count.most_common(2))

# 主程序逻辑
def main():
    txt_path = Path("data/week02_sentences.txt")
    lines = load_lines(txt_path)
    num_sentences = len(lines)

    sentence_info = []
    total_char = 0
    for sent in lines:
        char_count = len(sent)
        word_list = normalize_text(sent).split()
        word_count = len(word_list)
        total_char += char_count
        sentence_info.append({
            "text": sent,
            "char_num": char_count,
            "word_num": word_count
        })

    avg_length = round(total_char / num_sentences, 2)
    longest_5 = sorted(sentence_info, key=lambda x: x["char_num"], reverse=True)[:5]
    word_counter = count_tokens(lines)
    top_20 = word_counter.most_common(20)

    result_data = {
        "num_sentences": num_sentences,
        "avg_length": avg_length,
        "top_tokens": top_20,
        "longest_examples": longest_5
    }

    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "week02_stats.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    print("统计结果已保存至 outputs/week02_stats.json")

if __name__ == "__main__":
    main()
