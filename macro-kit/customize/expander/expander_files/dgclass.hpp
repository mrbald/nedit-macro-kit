class \1:
	public ty_drawableNodeBase
{
public:
	// construcor without ancestor
	\1\(
		ty_pt_nodeBase pt_father,
		ty_localID li,
		ty_repere ri);

	// with ancestor
	\1\(
		ty_pt_nodeBase pt_father,
		ty_localID li,
		ty_repere ri,
		ty_nodeBase& _ancestor);
	
	// death function
	void deathDay();
	
	/// generation
	virtual void upDown(parserFunction::ty_generation& v);
	
	/// \1 output.
	std::ostream& output(std::ostream& os) const;
	
	///  output operator.
	inline friend std::ostream& operator<<(std::ostream& os, const \1& obj)
	{ return obj.output(os); }

protected:
	/// next generation generation
	void childGeneration(parserFunction::ty_generation& v);
	
	/// opengl draw function
	void drawCore();
	
	/// opengl debug draw function
	void drawDebug(ty_glViewer&);

	/// set maturity
	void setMaturity(ty_visualProperty& vp);
	
	static \1* _\1\(ty_nodeBaseBase* pt)
	{
		return static_cast<\1*>(pt);
	}
	
	static \1& _\1\(ty_nodeBaseBase& ref)
	{
		return static_cast<\1&>(ref);
	}

}; // end of \1
