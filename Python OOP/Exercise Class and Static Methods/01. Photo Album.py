from math import ceil

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.buildphotos()

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for pages in range(self.pages):
            for position in range(PhotoAlbum.PHOTOS_PER_PAGE):
                if self.photos[pages][position] is None:
                    self.photos[pages][position] = label
                    return f"{label} photo added successfully on page {pages + 1} slot {position + 1}"

    def display(self):
        delimiter = '-' * 11
        result = ''
        for pages in self.photos:
            page_str = ' '.join(['[]' if self.photos is not None else '' for photo in self.pages])

    def buildphotos(self):
        result = []
        for _ in range(self.pages):
            result.append([None] * self.PHOTOS_PER_PAGE)
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
