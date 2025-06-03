import Card from 'react-bootstrap/Card';
import './CardWidget.css';

function CardWidget({ content, title, keywords, analyzed_by, date_creation, onCardClick, image_url }) {
  return (
    <div className='card-container' >
      <Card className='card-widget'>
          <Card.Img variant="top" src={image_url}  onClick={onCardClick}/>
        <div className='card-content' onClick={onCardClick}>
          <Card.Body>
            <Card.Title className='card-title'>
              <h1>{title}</h1>
            </Card.Title>
            <Card.Text>
              <ul>
                <li><b>Analyzed by</b>: {analyzed_by}</li>
                <li><b>Created at</b>: {date_creation}</li>
                <li>[{keywords.join(', ')}]</li>
              </ul>
              <p>{content.introduction}</p>
            </Card.Text>
          </Card.Body>
        </div>
      </Card>
    </div>
  )
}

export default CardWidget;
