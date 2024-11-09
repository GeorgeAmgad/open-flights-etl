class TransformationPipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def apply(self, data):
        for step in self.steps:
            data = step.apply(data)
            if data is None or data.empty:
                print(f"Warning: Step {step.__class__.__name__} returned invalid data.")
                continue
        return data
