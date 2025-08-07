def analyze_skin(image_path):
    import random
    skin_types = ['Normal', 'Oily', 'Dry', 'Combination', 'Sensitive']
    skin_type = random.choice(skin_types)

    emoji_map = {
        "Normal": "😊",
        "Oily": "🛢️",
        "Dry": "🌵",
        "Combination": "🔀",
        "Sensitive": "😬"
    }

    responses = {
        "Normal": {
            "recommendations": (
                "🧴 Maintain your natural balance with a simple skincare routine. "
                "Cleanse twice daily with a gentle, sulfate-free cleanser. Use a lightweight, non-comedogenic moisturizer. "
                "Don’t forget daily sunscreen to prevent aging. Weekly exfoliation with mild scrubs can help retain radiance."
            ),
            "eat": (
                "🥦 Green veggies (spinach, broccoli), 🥕 carrots, 🍎 apples, 💧 drink at least 2.5L water daily, "
                "and consume omega-rich foods like chia seeds and walnuts to maintain skin glow."
            ),
            "avoid": (
                "🍔 Junk food, 🧂 excessive salty snacks, 🧃 sugary sodas, and caffeine-heavy drinks that can disrupt hydration."
            ),
            "products": (
                "🌸 Aloe-based moisturizers, 🧼 gentle foam face wash, 🌿 rose water toner, and lightweight gel sunscreens (SPF 30+)."
            ),
            "home_remedies": (
                "🍯 Apply a honey and yogurt face mask weekly, 🥒 cucumber juice as toner, and 🌼 rose water mist for hydration boost."
            ),
            "ingredients_use": (
                "✅ Hyaluronic Acid, Vitamin C, Niacinamide, Panthenol, and Squalane."
            ),
            "ingredients_avoid": (
                "❌ Harsh exfoliants like walnut scrubs, Alcohol-based toners, Artificial fragrances."
            )
        },
        "Oily": {
            "recommendations": (
                "🧼 Cleanse twice a day with a salicylic acid-based face wash. "
                "Avoid over-cleansing as it can increase oil production. Use oil-free, mattifying moisturizers. "
                "Exfoliate 2-3 times a week with BHA-based products to prevent clogged pores. "
                "Never skip sunscreen — opt for gel-based, non-comedogenic SPF."
            ),
            "eat": (
                "🥒 Cucumber, 🍵 green tea, 🥗 fiber-rich salads, 🍋 lemon water, "
                "and 🥝 kiwi or citrus fruits to balance sebum production and reduce breakouts."
            ),
            "avoid": (
                "🍕 Greasy fast food, 🍫 chocolate (in excess), 🥤 sugary drinks, and 🌶 spicy food — all can trigger acne or oil build-up."
            ),
            "products": (
                "🧴 Oil-control toner, 🧼 clay-based face wash, 💦 niacinamide serum, matte finish moisturizers, "
                "and SPF 50 oil-free sunscreen."
            ),
            "home_remedies": (
                "🌿 Apply Multani mitti (Fuller's Earth) mixed with rose water twice a week. "
                "Use aloe vera gel as a natural moisturizer and ice cubes to reduce large pores."
            ),
            "ingredients_use": (
                "✅ Salicylic Acid, Niacinamide, Zinc, Tea Tree Oil, Bentonite Clay."
            ),
            "ingredients_avoid": (
                "❌ Coconut oil, Heavy creams, Alcohol-based astringents, Comedogenic oils."
            )
        },
        "Dry": {
            "recommendations": (
                "💧 Cleanse with cream-based hydrating cleansers. Apply thick moisturizers with occlusives like shea butter. "
                "Avoid long hot showers and harsh soaps. Incorporate facial oils at night. "
                "Use a humidifier in dry environments and never skip SPF to prevent flakiness and damage."
            ),
            "eat": (
                "🥑 Avocados, 🐟 fatty fish (salmon, mackerel), 🥜 nuts (almonds, walnuts), 🧈 olive oil, and 🍊 vitamin-C rich fruits for collagen production."
            ),
            "avoid": (
                "🍟 Fried foods, 🍺 alcohol, and 🧃 overly acidic juices that dehydrate skin. Avoid caffeine overdose."
            ),
            "products": (
                "🧴 Thick moisturizers (with ceramides or shea butter), 🧼 hydrating cleanser, 🧊 mist sprays, and creamy SPF moisturizers."
            ),
            "home_remedies": (
                "🥛 Milk and honey mask to lock moisture, 🥥 coconut oil massage before sleep, and oatmeal + yogurt pack weekly."
            ),
            "ingredients_use": (
                "✅ Glycerin, Shea Butter, Squalane, Ceramides, Hyaluronic Acid, Panthenol."
            ),
            "ingredients_avoid": (
                "❌ Benzoyl Peroxide, Retinoids (unless buffered), Sulfates, Alcohol."
            )
        },
        "Combination": {
            "recommendations": (
                "🌀 Focus on balancing — cleanse with a gentle gel-based face wash. Moisturize with lightweight gel on T-zone and cream on dry patches. "
                "Use masks targeting specific areas — clay mask on oily zones and hydration mask on dry zones. "
                "Use toner with balancing pH (5.5)."
            ),
            "eat": (
                "🍎 Apples, 🥬 spinach, 💧 at least 8 glasses of water, 🥕 carrots, and 🐟 omega-rich fish to maintain oil-water balance."
            ),
            "avoid": (
                "🍭 Sugary snacks, 🍔 oily food, ❌ dairy (if acne-prone), and too much caffeine — they can worsen both dry and oily zones."
            ),
            "products": (
                "🧴 Gel-based moisturizer, 🧼 mild foam cleanser, 🍃 green tea toner, and dual-action SPF cream."
            ),
            "home_remedies": (
                "🥒 Cucumber and aloe vera mask, 🍯 honey and turmeric spot treatment, and chilled green tea face spritz."
            ),
            "ingredients_use": (
                "✅ Niacinamide, Vitamin E, Hyaluronic Acid, Panthenol."
            ),
            "ingredients_avoid": (
                "❌ Heavy oils (like coconut oil), Synthetic fragrance, Over-drying alcohols."
            )
        },
        "Sensitive": {
            "recommendations": (
                "🧖‍♀️ Keep your skincare minimal. Use fragrance-free, hypoallergenic products. "
                "Avoid using too many new products at once. Patch test everything. Moisturize daily with barrier-repair creams. "
                "Avoid scrubs or chemical exfoliants unless dermatologist approved."
            ),
            "eat": (
                "🥕 Carrots, 🍌 bananas, 🥒 cucumbers, 🌰 almonds, and 🥥 coconut water to soothe inflammation and support the skin barrier."
            ),
            "avoid": (
                "🌶️ Spicy food, 🍺 alcohol, 🍫 excess sugar, and 🧂 processed foods — all can trigger sensitivity or redness."
            ),
            "products": (
                "🧴 Fragrance-free barrier repair creams, 🧼 Micellar water cleanser, 🧊 cooling mist, and mineral-based sunscreens (zinc oxide, titanium dioxide)."
            ),
            "home_remedies": (
                "🧊 Ice cube rub wrapped in cloth, 🌼 chamomile tea compress, 🥒 cold cucumber slices for calming flare-ups."
            ),
            "ingredients_use": (
                "✅ Aloe Vera, Ceramides, Centella Asiatica, Oat Extract, Panthenol."
            ),
            "ingredients_avoid": (
                "❌ Retinoids (unless prescribed), Essential Oils, Fragrance, Alcohol, Sulfates."
            )
        }
    }

    data = responses[skin_type]
    return {
        "skin_type": f"{skin_type} {emoji_map[skin_type]}",
        "recommendations": data["recommendations"],
        "what_to_eat": data["eat"],
        "what_to_avoid": data["avoid"],
        "products": data["products"],
        "home_remedies": data["home_remedies"],
        "ingredients_to_use": data["ingredients_use"],
        "ingredients_to_avoid": data["ingredients_avoid"]
    }


