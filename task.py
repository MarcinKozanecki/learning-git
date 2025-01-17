shopping_list={
    "piekarnia": ["chleb", "bułki", "pączki"],
    "warzywniak":["marchew", "seler","rukola"]
}

total_product=0
for shop in shopping_list:
    print("Ide do sklepu", shop.title(),"i kupuje tu następujące rzeczy", [product.title() for product in shopping_list[shop]])
    total_product+=len(shopping_list[shop])
print("w sumie kupuje", total_product,"produktów")