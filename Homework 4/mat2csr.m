function [IA,JA, AA] = mat2csr(A,varargin);
%Convert matrix from MATLAB coordinate format to CSR format. Optionally
%store sparsity information to file
%	A: input matrix 
%	varargin{1}:	output file
%	varargin{2}:	if A is adgacency matrix of graph G, then this is a
%			Nx2 array XY holding positions of nodes of the graph G
%	IA, JA, AA:	Arrays that hold A in CSR format (rows, columns and
%			elements respectively)
%	output file:	IA  and then JA or
%			IA, XY (XY(k,1) and XY(k,2) at each line k=1,...,N)
%			and then JA.
%	  
%	C. Bekas.
%	Version 1.0. Minneapolis, February 27th, 2004.

IA = zeros(size(A,1)+1,1);
JA = zeros(nnz(A)+1,1);
AA = zeros(nnz(A)+1,1);

flag = 0;
counter = 1;
%Go through all rows
for k=1:size(A,1)
    [IC, JC, CAA] = find(A(k,:));
    if isempty(CAA)
        %line is empty!
        flag = 1;
    else
        %handle previous line first
        if flag
            IA(k-1)=counter; 
            flag=0;
        end
        IA(k)=counter;
        JA(counter:counter + length(JC)-1)=JC;
        AA(counter:counter + length(JC)-1)=CAA;
        counter = counter + length(JC);
    end
end
IA(end)=IA(1)+nnz(A);

if nargin==2
    if ~(strcmp('char',class(varargin{1})))
        error('2nd argument must be a string that holds a filename');
    end    
    fl=varargin{1};
    fd=fopen(fl,'rw');
    if fd<0
        error('Error opening input file!');
    end    
    fprintf(fd,'%d %d\n', size(A,1), nna(A));
    for k=1:length(IA)
        fprintf(fd,'%d\n',IA(k));
    end
    for k=1:length(JA)
        fprintf(fd,'%d\n',JA(k));
    end
    fclose(fl);
end

if nargin==3
    if ~(strcmp('char',class(varargin{1})))
        error('2nd argument must be a string that holds a filename');
    end        
    if ~(strcmp('double',class(varargin{2})))
        error('3rd argument must be a Nx2 array that holds the geometric positions of the nodes');
    end
    if ( (size(varargin{2},1)~=size(A,1)) | (size(varargin{2},2)~=2) )
        error('3rd argument must be a Nx2 array that holds the geometric positions of the nodes');
    end
    xy=varargin{2};
    fl=varargin{1};
    fd=fopen(fl,'w+');
    if fd<0
        error('Error opening input file!');
    end
    fprintf(fd,'%d %d\n', size(A,1), nnz(A));
    for k=1:length(IA)
        fprintf(fd,'%d\n',IA(k));
    end
    for k=1:size(A,1)
        fprintf(fd,'%d %d\n',xy(k,1), xy(k,2));
    end
    for k=1:length(JA)
        fprintf(fd,'%d\n',JA(k));
    end
    fclose(fd);
end

    
