# Best-Buy

A simple Python-based store simulator for practicing working with inventory, products, and customer orders from the command line. Focused on learning object-oriented programming, input validation, and fundamental business logic.

## Features

- **Product Management:** Built-in store with example inventory
- **Order Simulation:** Choose items, set quantities, and make orders interactively
- **Stock Tracking:** See remaining quantity after purchases
- **Inventory Overview:** List all available products and their current stock
- **Total Quantity Calculation:** Know how many items are left in the store

## Project Structure

Best-Buy/  
├── main.py # Main app logic and menu  
├── product.py # Product class and helpers  
├── store.py # Store class and inventory/order management  
└── **pycache**/ # Python bytecode cache (ignore)

## Getting Started

1. **Clone the repository:**
```bash
git clone https://github.com/Miami05/Best-Buy.git
```
```bash
cd Best-Buy
```

2. **Run the main script:**
```bash
python main.py
```
- This opens a menu to view products, see store totals, or make orders.

3. **Follow the prompts:**
- Choose products by number, enter desired quantity, and make an order.
- View real-time updates to stock after a purchase.

## Usage

- **Add new products** by editing the `main()` function inside `main.py`.
- The menu lets you:
- List all store products (with price and quantity)
- Show total quantity in store
- Make an order (simulates a shopping cart and checkout)
- Quit the program

## Example Products

- Bose Headphones: \$250, quantity 500
- MacBook Air M2: \$1450, quantity 100

## Customization

- Add/remove products by editing the list in `main.py`
- Extend `Product` and `Store` classes with more features or product types

## License

Open-source; feel free to reuse or adapt for learning purposes.

Use Best-Buy to practice Python classes, input, and interaction in a fun, realistic context!
