import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import { Fragment } from 'react';

function App() {
  const [data, setData] = useState({ num: -1, comments: [] });
  const [inputValue, setInputValue] = useState('');
  const [username, setUsername] = useState('');
  const [comment, setComment] = useState('');


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:5000/api/data");
        setData(response.data);
        console.log(response.data);
      } catch (error) {
        console.error('There was an error fetching the data!', error);
      }
    };

    fetchData();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const formData = new FormData();
      formData.append('fact', inputValue);

      const response = await axios.post('http://localhost:5000/getFact', formData);
      setData(response.data);
      console.log(response.data);
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  const handleCommentSubmit = async (e) => {
    e.preventDefault();
    try {
      const formData = new FormData();
      formData.append('username', username);
      formData.append('comment', comment);
      const response = await axios.post('http://localhost:5000/comment', formData);
      setData(response.data);
      console.log(response.data);
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  console.log(data.comments);

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>Enter number</label>
        <br />
        <input
          type="text"
          name="fact"
          required
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <br />
        <button type="submit" class="btn btn-success">Get factorial</button>
      </form>
      <br />
      <h1>The factorial is {data.num}</h1>
      <br />
      <br />
      <br />
      <br />
      <form onSubmit={handleCommentSubmit}>
        <label>Name</label>
        <br />
        <input 
          type="text"
          name="username" 
          required
          value={username}
          onChange={(e) => setUsername(e.target.value)} 
        />
        <br />
        <label>Leave comment</label>
        <br />
        <textarea 
          name="comment" 
          style={{height: "150px", width: '300px'}} 
          required 
          value={comment}
          onChange={(e) => setComment(e.target.value)} 
        />
        <br />
        <button type="submit" className="btn btn-success">Post comment</button>
      </form>
      <br />
      <br />
      <h1>Comments: </h1>
      <br />
      <div id="comments_container">
        {data.comments.map(item => (
          <Fragment>
            <hr />
            <h5>{item[0]}</h5>
            <p>{item[1]}</p>
          </Fragment>
        ))}
        <hr />
      </div>
    </div>
  );
}

export default App;
