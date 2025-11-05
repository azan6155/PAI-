class Photo:
    def __init__(self, matrix):
        self.matrix = matrix

    def clone(self):
        return [[val for val in row] for row in self.matrix]

    def apply(self, func):
        self.matrix = func(self.matrix)


def mirror_horizontal(data):
    return [list(reversed(row)) for row in data]


def change_brightness(data, offset):
    return [[val + offset for val in row] for row in data]


def rotate_90(data):
    r, c = len(data), len(data[0])
    result = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(data[r - j - 1][i])
        result.append(row)
    return result


class TransformPipeline:
    def __init__(self):
        self.transforms = []

    def add(self, func):
        self.transforms.append(func)

    def run(self, image):
        results = []
        for func in self.transforms:
            new_photo = Photo(image.clone())
            new_photo.apply(func)
            results.append(new_photo)
        return results


if __name__ == "__main__":
    base_pixels = [
        [10, 20, 30],
        [40, 50, 60]
    ]

    photo = Photo(base_pixels)
    pipeline = TransformPipeline()
    pipeline.add(mirror_horizontal)
    pipeline.add(lambda m: change_brightness(m, 10))
    pipeline.add(rotate_90)

    output_images = pipeline.run(photo)

    print("Original Image:")
    for r in photo.matrix:
        print(r)

    print("\nGenerated Variations:")
    for i, img in enumerate(output_images, start=1):
        print(f"Variation {i}:")
        for r in img.matrix:
            print(r)
        print()
