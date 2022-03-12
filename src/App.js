/* eslint-disable no-return-assign */
/* eslint-disable no-shadow */
/* eslint-disable react/jsx-filename-extension */
/* eslint-disable react/react-in-jsx-scope */
/* eslint-disable no-undef, no-alert */
import { useState, useEffect, useRef } from 'react';
import './App.css';

function App() {
  const [reviews, setReviews] = useState([]);
  const reviewsToEdit = useRef([]);
  const reviewsToDelete = useRef([]);
  useEffect(() => {
    fetch('/movie_comments', {
      headers: {
        "content_type":"application/json",
      },
    }).then((response) => response.json()).then((data) => setReviews(data));
  }, []);

  reviewsToEdit.current = reviews;

  function deleteReview(review) {
    reviewsToDelete.current.push(review);
    alert(`You will delete the movie review: ${review.movie_id} and the rating: ${review.rating} ${review.comment}\n Clicking save changes will apply this`);
  }

  function sendNewReviews() {
    fetch('/edit_reviews', {
      method: 'POST',
      cache: 'no-cache',
      headers: {
        content_type: 'application/json',
      },
      body: JSON.stringify(reviewsToEdit.current),
    }).then((response) => response.json()).then((data) => {
      if (data.SUCCESS === 'TRUE') {
        alert('Change Successful');
      }
    });
  }

  function sendDeleteReviews() {
    fetch('/delete_reviews', {
      method: 'POST',
      cache: 'no-cache',
      headers: {
        content_type: 'application/json',
      },
      body: JSON.stringify(reviewsToDelete.current),
    }).then((response) => response.json()).then((data) => {
      if (data.SUCCESS === 'TRUE') {
        alert('Delete Succesful');
      }
    });
  }

  function buttonHandler() {
      sendNewReviews();
      sendDeleteReviews();
  }

  return (
    <div className="App">
      
      <body>
      <header className="App-header">
        <h1>Reviews:</h1>

        {reviews && reviews.map((reviews, index) => (
          <div>
            <p>
              Movie:
              {reviews.movie_id}
            </p>
           
            <p>
              Username:
              {reviews.username}
            </p>
            <input type="number" name="rating" min="1" max="5" defaultValue={reviews.rating} onChange={(e) => reviewsToEdit.current[index].rating = e.target.value} />
            <input type="text" name="comment" defaultValue={reviews.comment} onChange={(e) => reviewsToEdit.current[index].comment = e.target.value} />
            <button type="button" onClick={() => deleteReview(reviews)}>Delete!</button>
            <br />
          </div>
        ))}

        <br />

        <button type="button" value="SAVE CHANGES" onClick={buttonHandler}>Save Changes!</button>
        <br></br>
        <a href="/home">Link to Homepage</a>
        </header>
        
      </body>
      
    </div>
  );
}

export default App;
