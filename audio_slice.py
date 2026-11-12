from pydub import AudioSegment


# 入力ファイル名
INPUT_FILE = "python-audio-output.wav"

# 出力ファイル名
OUTPUT_FILE_BEFORE = "audio-output-before.wav"
OUTPUT_FILE_AFTER = "audio-output-after.wav"

# 音声を分割する位置（ミリ秒）
SPLIT_MS = 4000


def main():
    """音声ファイルを4秒の位置で分割して保存する。"""
    # WAVファイルを読み込む
    # from_file() は WAV 以外の形式にも対応できる
    audio = AudioSegment.from_file(INPUT_FILE, format="wav")

    # 先頭から4秒までを抽出する
    audio_before = audio[:SPLIT_MS]

    # 抽出した音声を WAV ファイルとして保存する
    audio_before.export(OUTPUT_FILE_BEFORE, format="wav")

    # 4秒以降の音声を抽出する
    audio_after = audio[SPLIT_MS:]

    # 抽出した音声を WAV ファイルとして保存する
    audio_after.export(OUTPUT_FILE_AFTER, format="wav")

    print("音声が4秒の位置で分割され、WAVファイルとして保存されました。")


if __name__ == "__main__":
    main()
