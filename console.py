import pdb
from models.video import Video
from models.director import Director

import repositories.video_repository as video_repository
import repositories.director_repository as director_repository

video_repository.delete_all()
director_repository.delete_all()

director1 = Director("Steven Spielberg", "0776494323")
director_repository.save(director1)
director2 = Director("Christopher Nolan", "0774356323")
director_repository.save(director2)
director3 = Director("Stanley Kubrick", "0774593827")
director_repository.save(director3)

director_repository.select_all()

video_1 = Video("Jaws", "Horror", "Hero shark gets cancelled for being too 'real'.", 10, 2, 5, director1)
video_repository.save(video_1)
video_2 = Video("Batman Begins", "Superhero", "Billionaire beats the underprivileged because bat.", 15, 2, 5, director2)
video_repository.save(video_2)
video_3 = Video("Titanic", "Romance", "Everyone enjoys an ice-bucket challenge", 20, 2, 5, director1)
video_repository.save(video_3)
video_4 = Video("Inception", "Thriller", "Just sleeping basically", 8, 2, 5, director2)
video_repository.save(video_4)
video_5 = Video("The Shining", "Horror", "Airbnb gone wrong.", 13, 2, 5, director3)
video_repository.save(video_5)
video_6 = video()




pdb.set_trace()