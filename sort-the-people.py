class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_name: List[Tuple[int, str]] = []

        for name, hight in zip(names, heights):
            sorted_name.append((hight, name))

        sorted_name.sort(reverse=True)
        answer: List[str] = []
        for hight, name in sorted_name:
            answer.append(name)
        return answer
