from pyraac.utils.read import _read_fasta


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
    def __init__(self, file_path=None):
        self.titles = None
        self.sequences = None
        self.behavior_cache_reduction = []

        if file_path is not None:
            self.titles, self.sequences = _read_fasta(file_path)

    def read_fasta(self, file_path):
        self.titles, self.sequences = _read_fasta(file_path)
