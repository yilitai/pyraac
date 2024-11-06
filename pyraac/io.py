class BehaviorReduction:
    def __init__(
        self,
        start_index,
        end_index,
        sequence_index,
        raaValue,
    ):
        self.start_index = start_index
        self.end_index = end_index
        self.sequence_index = sequence_index
        self.raaValue = raaValue


class SequenceBundle:
    def __init__(self):
        self.titles = None
        self.sequences = None
        self.behavior_cache_reduction = []

    def read_fasta(self, file_path):
        temp_title_list = []
        temp_sequence_list = []

        current_sequence = ""

        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith(">"):
                    if current_sequence:  # 如果当前序列不为空，保存上一个序列
                        temp_sequence_list.append(current_sequence)
                        current_sequence = ""
                    temp_title_list.append(line[1:])  # 保存标题，去掉开头的 '>'
                else:
                    current_sequence += line  # 追加序列数据

            if current_sequence:  # 文件结束时，保存最后一个序列
                temp_sequence_list.append(current_sequence)

        self.titles = temp_title_list
        self.sequences = temp_sequence_list
