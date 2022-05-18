
# Opening the file 
open(fh, "../raw-data/snippet.tmx") or die "File '$filename' can't be opened";
  
while (<fh>) {
      if ("<seg>(.?*)</seg>") {
        print "$1\n";
      }
      else {
          print "not found\n";
      }
   
}
