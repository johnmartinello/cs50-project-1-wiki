# cs50 project 1 wiki

### Entry Page: 
- Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry,  render a page that displays the contents of that encyclopedia entry.
- The view  get the content of the encyclopedia entry by calling the appropriate util function.
- If an entry is requested that does not exist, the user is be presented with an error page indicating that their requested page was not found.
- If the entry does exist, the user is be presented with a page that displays the content of the entry. 
- The title of the page  include the name of the entry.
### Index Page:
- user can click on any entry name to be taken directly to that entry page.
### Search:
- Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
- If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.
- If the query does not match the name of an encyclopedia entry, the user is taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.
- Clicking on any of the entry names on the search results page should take the user to that entry’s page.
### New Page:
- Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry.
- Users are able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
- Users are to click a button to save their new page.
- When the page is saved, if an encyclopedia entry already exists with the provided title, the user is presented with an error message.
- Otherwise, the encyclopedia entry is saved to disk, and the user is taken to the new entry’s page.
### Edit Page:
- On each entry page, the user is able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
- The textarea is pre-populated with the existing Markdown content of the page..
- The user is able to click a button to save the changes made to the entry.
- Once the entry is saved, the user is redirected back to that entry’s page.
### Random Page: 
- Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
