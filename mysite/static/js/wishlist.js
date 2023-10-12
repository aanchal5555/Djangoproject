let wishlist = []; // Initialize an empty wishlist array

  // Function to add a product to the wishlist
  function addToWishlist(productId) {
      if (!wishlist.includes(productId)) {
          wishlist.push(productId);
          updateWishlistButton();
      }
  }
  
  // Function to update the display wishlist button
  function updateWishlistButton() {
      const displayWishlistButton = document.querySelector('.action-btn .count');
      displayWishlistButton.textContent = wishlist.length;
  }
  
  // Add event listeners for the "add to wishlist" buttons
  const addToWishlistButtons = document.querySelectorAll('.btn-action');
  addToWishlistButtons.forEach(button => {
      button.addEventListener('click', () => {
          const productId = button.getAttribute('data-product-id');
          addToWishlist(productId);
      });
  });