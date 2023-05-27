// Sample data for recently played tracks
const recentTracks = [
    {
      title: "Song 1",
      artist: "Artist 1",
      album: "Album 1",
      image: "https://example.com/image1.jpg"
    },
    {
      title: "Song 2",
      artist: "Artist 2",
      album: "Album 2",
      image: "https://example.com/image2.jpg"
    },
    {
      title: "Song 3",
      artist: "Artist 3",
      album: "Album 3",
      image: "https://example.com/image3.jpg"
    }
  ];
  
  // Get the recent tracks list element
  const recentTracksList = document.getElementById("recent-tracks");
  
  // Loop through the recent tracks and add them to the list
  for (let i = 0; i < recentTracks.length; i++) {
    const track = recentTracks[i];
    
    // Create a new list item for the track
    const li = document.createElement("li");
    
    // Add the track information to the list item
    li.innerHTML = `
      <img src="${track.image}" alt="${track.album}">
      <div>
        <p>${track.title}</p>
        <p>${track.artist} - ${track.album}</p>
      </div>
    `;
    
    // Add the list item to the recent tracks list
    recentTracksList.appendChild(li);
  }
  