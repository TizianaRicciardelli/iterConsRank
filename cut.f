      program aaa
      implicit real*8 (a-h,o-z)
      character*40 FileName(10000)
      ! read the percentage of files
      open(101,file='cut',status='old')
      read(101,*)percentage


      open(102,file='Zscore.txt',status='old')
      nlen=1
      do while(.true.)
        read(102,*,end=901)FileName(nlen)
        nlen=nlen+1
      enddo
 901  continue
      nlen=nlen-1

      write(*,*)"At this step, you have ",nlen,"files in total"
      n1=nint(percentage*dble(nlen))
      write(*,*)"We will keep ",n1,"files "

      open(201,file='temp')
      write(201,*)"NumberOfPDBFiles",n1
      do i=nlen-n1+1,nlen
        write(201,*)FileName(i)
      enddo
      end
