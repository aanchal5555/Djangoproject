
    $(document).ready(function () {
        // Check if the 'cart' object is in localStorage and initialize it if not
        var cart = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : {};

        // Function to update the cart count displayed in the header
        function updateCartCount() {
            var cartCount = Object.keys(cart).length;
            $('#cart-count').text(cartCount);
        }

        // Click event handler for the "Add to Cart" button with the 'cart' class
        $('.cart').click(function () {
            // Perform the logic to add an item to the cart (you can adapt your existing code here)
            var idstr = 'product_id'; // Replace with the actual product ID
            if (cart[idstr] !== undefined) {
                cart[idstr] = cart[idstr] + 1;
            } else {
                cart[idstr] = 1;
            }

            // Save the updated cart to localStorage
            localStorage.setItem('cart', JSON.stringify(cart));

            // Update the cart count display
            updateCartCount();
        });

        // Initialize the cart count display
        updateCartCount();
    });

