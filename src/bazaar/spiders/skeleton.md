## Current auctions

Current auctions page skeleton

- `<div class="InnerTableContainer">` - Table container with paginated auctions
  - `<tr>` - First table row has the page navigation and total results. The following has the auctions
    - `<div class="Auction">` - Actual auction container
      - `<div class="AuctionHeader">` - Character level, vocation, sex and world separated by `|`
        - `<div class="AuctionCharacterName">` - Character name and link in `<a>` tag
      - `<div class="AuctionBody">` - Sales arguments
        - `<div class="AuctionBodyBlock AuctionDisplay AuctionOutfit">`
        - `<div class="AuctionBodyBlock AuctionDisplay AuctionItemsViewBox">`
        - `<div class="AuctionBodyBlock ShortAuctionData">` - Auction duration and current price
        - `<div class="AuctionBodyBlock SpecialCharacterFeatures">` - Character features
          - `<div class="Entry">` - Feature text + icon in `<img>` tag