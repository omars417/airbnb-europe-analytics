# Feature Dictionary

This document describes every feature created during the Silver Layer.

---

## price_per_guest

Formula

price / person_capacity

Purpose

Measures the price paid per guest.

Business Value

Allows comparison between listings with different capacities.

---

## price_per_bedroom

Formula

price / bedrooms

Purpose

Measures cost efficiency relative to the number of bedrooms.

Business Value

Useful for comparing apartments of different sizes.

---

## distance_category

Source

dist

Categories

- City Center
- Near Center
- Far

Business Value

Groups listings by distance to the city center.

---

## metro_accessibility

Source

metro_dist

Categories

- Excellent
- Good
- Limited

Business Value

Measures accessibility to public transportation.

---

## luxury_listing

Definition

Top 10% of listings ranked by price.

Values

True / False

Business Value

Segments premium listings.

---

## city_price_tier

Definition

Average city price ranking.

Values

High

Medium

Low

Business Value

Allows comparison between expensive and affordable cities.
