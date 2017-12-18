
class System:

    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules

    def _get_str(self, last_str):
        new_str = ''
        for char in last_str:
            if char in self.rules:
                new_str += self.rules[char]
            else:
                new_str += char
        return new_str

    def get_str(self, num_iterations):
        string = self.axiom
        for i in range(num_iterations):
            string = self._get_str(string)
        return string

