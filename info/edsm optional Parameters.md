

- showId	0
  - Set to 1 to get our internal ID for this system.
- showCoordinates	0
  - Set to 1 to get the system coordinates.
    If coordinates are unknown, the coords key will not be returned.
- showPermit	0
  - Set to 1 to get the system permit if there is one.
    If the permit is named, also return permitName.
- showInformation	0
  - Set to 1 to get the system information like allegiance, government...
    If no information are stored, an empty array will be returned.
- showPrimaryStar	0
  - Set to 1 to get the system primary star if known.
    If no primary star is stored, a NULL will be returned.
- includeHidden	0
  - Set to 1 to get system even if hidden in the database.
    Hidden system are generally typo errors, renamed system in the game...
