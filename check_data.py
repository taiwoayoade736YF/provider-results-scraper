
import csv

with open("books.csv", "r", newline="", encoding="utf-8-sig") as file:
    books = list(csv.DictReader(file))

required_fields = ["name", "price", "url"]

missing_values = 0

for book in books:
    for field in required_fields:
        if not book.get(field, "").strip():
            missing_values += 1
            print(f"Missing {field}: {book}")

unique_books = {
    (book["name"], book["price"], book["url"])
    for book in books
}

print("\n--- Data Quality Report ---")
print(f"Total records: {len(books)}")
print(f"Unique records: {len(unique_books)}")
print(f"Duplicate records: {len(books) - len(unique_books)}")
print(f"Missing values: {missing_values}")
