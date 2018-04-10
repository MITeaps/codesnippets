# Import PdfPages 
from matplotlib.backends.backend_pdf import PdfPages
# Create blank PDF
pp = PdfPages('figures.pdf')

# Example data for plotting
x = np.linspace(0,5,10)
y1 = x
y2 = x**2

# Create linear plot
plt.plot(x,y1,'.');
# Save to pdf file
pp.savefig()

# Create parabolic plot
plt.figure();
plt.plot(x,y2,'.');

# Save to pdf file
pp.savefig()

# Once you have added every figure you want to the pdf,
# close the file
pp.close()
