import { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import CardWidget from './component/CardWidget';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Popup from 'reactjs-popup';
import { TextField } from '@mui/material';

function App() {
  const [message, setMessage] = useState('');
  const [newsList, setNewsList] = useState([]);

  const [showpopUpNews, setShowPopUp] = useState(false);
  const [selectedNews, setSelectedNews] = useState(null);
  const [trendInfo, setTrendInfo] = useState(false);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/news/')
      .then(res => {
        setNewsList(res.data);
      })
      .catch(err => console.error(err));
  }, []);

  const handlePopUpClick = (news) => {
    setSelectedNews(news);
    setShowPopUp(true);
  };

  const handleClosePopUp = () => {
    setShowPopUp(false);
    setSelectedNews(null);
  };

  const filteredNews = newsList.filter(news =>
    news.title.toLowerCase().includes(message.toLowerCase()) ||
    news.keywords.join(', ').toLowerCase().includes(message.toLowerCase())
  );

  return (
    <>
      <div className='container'>
        <div>
          <h1 style={{ fontSize: '5rem', marginTop: '10rem', marginBottom: '4rem' }}>Trending News</h1>
        </div>

        <TextField
          label='Search News'
          variant='outlined'
          onChange={(e) => setMessage(e.target.value)}
          sx={{ 
            marginBottom: '10rem',
            width: '700px', 
            input: {color: 'white'}, 
            label: {color: 'white'}, 
            '& .MuiOutlinedInput-root': {
              '& fieldset': {
                borderColor: 'white',
              },
              '&:hover fieldset': {
                borderColor: 'white',
              },
              '&.Mui-focused fieldset': {
                borderColor: 'white',
              },
            }
  
          }}
        />

        <div className="cards-wrapper">
          {filteredNews.map((news, index) => (
            <CardWidget
              key={index}
              content={news.content}
              title={news.title}
              keywords={news.keywords}
              analyzed_by={news.analyzed_by}
              date_creation={news.date_creation}
              onCardClick={() => handlePopUpClick(news)}
              image_url={news.image_url}
            />
          ))}
        </div>
      </div>

      {showpopUpNews && selectedNews && (
        <div className='popup-overlay' onClick={handleClosePopUp}>
          <div className='popup-content' onClick={(e) => e.stopPropagation()}>
            <button className='popup-close' onClick={handleClosePopUp}>X</button>

            <h1>{selectedNews.title}</h1>
            <img src={selectedNews.image_url} />
            <ul>
              <li><b>Analyzed by</b>: {selectedNews.analyzed_by}</li>
              <li><b>Date</b>: {selectedNews.date_creation}</li>
              <li>
                Trend value: {selectedNews.trend_score}/100
                <span
                  style={{ color: 'rgb(157, 192, 212)', cursor: 'pointer', marginLeft: '5px' }}
                  onClick={() => setTrendInfo(!trendInfo)}
                >
                  ...
                </span>
                {trendInfo && (
                  <p>
                    {selectedNews.trend_explanation}
                    <br />
                  </p>
                )}
              </li>
              <li><b>Keywords</b>: [{selectedNews.keywords.join(', ')}]</li>
            </ul>
            <p>{selectedNews.content.introduction}</p>
            <p>{selectedNews.content.body}</p>
            <p>{selectedNews.content.conclusion}</p>
            <br />
          </div>
        </div>
      )}
    </>
  );
}

export default App;
