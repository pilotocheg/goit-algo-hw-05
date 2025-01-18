import timeit
from algorithms.boyer_moore_search import boyer_moore_search
from algorithms.kmp_search import kmp_search
from algorithms.rabin_karp_search import rabin_karp_search
from pathlib import Path

article_1_path = Path(__file__).parent / "txt" / "article_1.txt"
article_2_path = Path(__file__).parent / "txt" / "article_2.txt"
article_1 = article_1_path.read_text(encoding="1251")
article_2 = article_2_path.read_text(encoding="utf-8")
article_1_pattern = "тоді програмісту слід розробити новий алгоритм або поміркувати"
article_2_pattern = "Блоки малого розміру зменшують втрати пам’яті"
not_exist_pattern = "Якийсь не існуючий текст"


def test_search_performance(fn_name):
    art_1_time = timeit.timeit(
        f"{fn_name}(article_1, article_1_pattern)",
        setup=(f"from __main__ import {fn_name}, article_1, article_1_pattern"),
        number=1,
    )
    art_1_time_not_found = timeit.timeit(
        f"{fn_name}(article_1, not_exist_pattern)",
        setup=(f"from __main__ import {fn_name}, article_1, not_exist_pattern"),
        number=1,
    )
    art_2_time = timeit.timeit(
        f"{fn_name}(article_2, article_2_pattern)",
        setup=(f"from __main__ import {fn_name}, article_2, article_2_pattern"),
        number=1,
    )
    art_2_time_not_found = timeit.timeit(
        f"{fn_name}(article_2, not_exist_pattern)",
        setup=(f"from __main__ import {fn_name}, article_2, not_exist_pattern"),
        number=1,
    )

    return [art_1_time, art_1_time_not_found, art_2_time, art_2_time_not_found]


def main():
    # value is (name, time)
    fastest = {
        "art_1": None,
        "art_2": None,
        "art_1_np": None,
        "art_2_np": None,
    }

    for fn in [boyer_moore_search, kmp_search, rabin_karp_search]:
        fn_name = fn.__name__
        [art_1_time, art_1_time_not_found, art_2_time, art_2_time_not_found] = (
            test_search_performance(fn_name)
        )
        print(f"Fn {fn_name} performance results:")
        print(f"Article 1 time (pattern found):", art_1_time)
        print(f"Article 2 time (pattern found):", art_2_time)
        print(f"Article 1 time (pattern not found):", art_1_time_not_found)
        print(f"Article 2 time (pattern not found):", art_2_time_not_found, "\n")

        if not fastest["art_1"] or art_1_time < fastest["art_1"][1]:
            fastest["art_1"] = (fn_name, art_1_time)
        if not fastest["art_2"] or art_2_time < fastest["art_2"][1]:
            fastest["art_2"] = (fn_name, art_2_time)
        if not fastest["art_1_np"] or art_1_time_not_found < fastest["art_1_np"][1]:
            fastest["art_1_np"] = (fn_name, art_1_time_not_found)
        if not fastest["art_2_np"] or art_2_time_not_found < fastest["art_2_np"][1]:
            fastest["art_2_np"] = (fn_name, art_2_time_not_found)

    print("Fastest for article 1:", fastest["art_1"])
    print("Fastest for article 2:", fastest["art_2"])
    print("Fastest for article 1 (pattern not found):", fastest["art_1_np"])
    print("Fastest for article 2 (pattern not found):", fastest["art_2_np"])


if __name__ == "__main__":
    main()
